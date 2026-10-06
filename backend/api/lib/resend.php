<?php
declare(strict_types=1);

require_once __DIR__ . '/env.php';

/**
 * Sends transactional email through the Resend HTTP API (no SDK / Composer needed).
 * Returns [success(bool), errorMessage(?string)].
 */
function resend_send_email(string $toEmail, string $subject, string $htmlBody, ?string $replyTo = null): array
{
    $apiKey = env('RESEND_API_KEY');
    $fromEmail = env('RESEND_FROM_EMAIL', 'Herger\'s & Co. Website <no-reply@notifications.hergerandco.com>');

    if (filter_var($toEmail, FILTER_VALIDATE_EMAIL) === false) {
        error_log('[resend] Refusing to send: destination address "' . $toEmail . '" is not a valid email (check COMPANY_EMAIL).');
        return [false, 'Email service is not configured correctly.'];
    }

    if ($apiKey === '' || str_starts_with($apiKey, 're_xxxx')) {
        error_log('[resend] RESEND_API_KEY is not configured — email not sent.');
        return [false, 'Email service is not configured yet.'];
    }

    $payload = [
        'from' => $fromEmail,
        'to' => [$toEmail],
        'subject' => $subject,
        'html' => $htmlBody,
    ];
    if ($replyTo !== null && $replyTo !== '') {
        $payload['reply_to'] = $replyTo;
    }

    $ch = curl_init('https://api.resend.com/emails');
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => json_encode($payload, JSON_THROW_ON_ERROR),
        CURLOPT_HTTPHEADER => [
            'Authorization: Bearer ' . $apiKey,
            'Content-Type: application/json',
        ],
        CURLOPT_TIMEOUT => 10,
    ]);

    $response = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $curlError = curl_error($ch);
    curl_close($ch);

    if ($response === false || $curlError !== '') {
        error_log('[resend] cURL error: ' . $curlError);
        return [false, 'Could not reach the email service.'];
    }
    if ($httpCode < 200 || $httpCode >= 300) {
        error_log('[resend] API error (' . $httpCode . '): ' . $response);
        return [false, 'The email service rejected the message.'];
    }

    return [true, null];
}
