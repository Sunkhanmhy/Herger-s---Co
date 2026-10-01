<?php
declare(strict_types=1);

require_once __DIR__ . '/env.php';

/** Sends a uniform JSON response and exits — every endpoint funnels through here. */
function json_response(bool $ok, string $message, int $statusCode = 200): never
{
    http_response_code($statusCode);
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode(['ok' => $ok, 'message' => $message], JSON_THROW_ON_ERROR);
    exit;
}

/** Locks down CORS to the configured allow-list; same-origin requests are always fine. */
function apply_cors_headers(): void
{
    $allowed = array_filter(array_map('trim', explode(',', env('ALLOWED_ORIGINS'))));
    $origin = $_SERVER['HTTP_ORIGIN'] ?? '';
    if ($origin !== '' && in_array($origin, $allowed, true)) {
        header('Access-Control-Allow-Origin: ' . $origin);
        header('Vary: Origin');
    }
    header('Access-Control-Allow-Methods: POST, OPTIONS');
    header('Access-Control-Allow-Headers: Content-Type, Accept');

    if (($_SERVER['REQUEST_METHOD'] ?? '') === 'OPTIONS') {
        http_response_code(204);
        exit;
    }
}

function require_post_method(): void
{
    if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
        json_response(false, 'Method not allowed.', 405);
    }
}

/** Silent honeypot check: bots that fill the hidden field are told "success" and dropped. */
function is_honeypot_triggered(array $fields): bool
{
    $field = env('FORM_HONEYPOT_FIELD', 'hp_confirm');
    return trim((string) ($fields[$field] ?? '')) !== '';
}

function sanitize_text(string $value, int $maxLength = 2000): string
{
    $value = trim($value);
    $value = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F]/', '', $value) ?? '';
    return mb_substr($value, 0, $maxLength);
}

function is_valid_email(string $email): bool
{
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false && strlen($email) <= 254;
}

/**
 * Very small file-based rate limiter (defense in depth, not a substitute for
 * a real WAF/rate-limiter at the edge). Allows N submissions per IP per window.
 */
function enforce_rate_limit(string $bucket, int $maxAttempts = 5, int $windowSeconds = 600): void
{
    $ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
    $dir = sys_get_temp_dir() . '/hergerandco_ratelimit';
    if (!is_dir($dir)) {
        mkdir($dir, 0700, true);
    }
    $file = $dir . '/' . preg_replace('/[^a-zA-Z0-9_.-]/', '_', $bucket . '_' . $ip) . '.json';

    $now = time();
    $attempts = [];
    if (is_readable($file)) {
        $decoded = json_decode((string) file_get_contents($file), true);
        if (is_array($decoded)) {
            $attempts = $decoded;
        }
    }
    $attempts = array_values(array_filter($attempts, static fn ($ts) => $ts > $now - $windowSeconds));

    if (count($attempts) >= $maxAttempts) {
        json_response(false, 'Too many submissions. Please try again later.', 429);
    }

    $attempts[] = $now;
    file_put_contents($file, json_encode($attempts), LOCK_EX);
}

function e(string $value): string
{
    return htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8');
}
