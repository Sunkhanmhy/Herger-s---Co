<?php
declare(strict_types=1);

/**
 * Minimal .env loader (no Composer dependency). Reads KEY=VALUE pairs,
 * ignores comments/blank lines, strips surrounding quotes. Real secrets
 * belong only in the untracked .env file — see .env.example for the schema.
 */
function env_load(string $path): void
{
    static $loaded = false;
    if ($loaded || !is_readable($path)) {
        return;
    }
    $loaded = true;

    $lines = file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    if ($lines === false) {
        return;
    }

    foreach ($lines as $line) {
        $line = trim($line);
        if ($line === '' || str_starts_with($line, '#')) {
            continue;
        }
        $parts = explode('=', $line, 2);
        if (count($parts) !== 2) {
            continue;
        }
        [$key, $value] = $parts;
        $key = trim($key);
        $value = trim($value);
        if (strlen($value) >= 2 && $value[0] === '"' && str_ends_with($value, '"')) {
            $value = substr($value, 1, -1);
        }
        if (getenv($key) === false) {
            putenv("{$key}={$value}");
        }
    }
}

function env(string $key, string $default = ''): string
{
    $value = getenv($key);
    return $value === false ? $default : $value;
}

env_load(dirname(__DIR__, 2) . '/.env');
