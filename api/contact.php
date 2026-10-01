<?php
declare(strict_types=1);

require_once __DIR__ . '/lib/security.php';
require_once __DIR__ . '/lib/resend.php';

apply_cors_headers();
require_post_method();
enforce_rate_limit('contact', 6, 600);

$fields = $_POST;
if (is_honeypot_triggered($fields)) {
    json_response(true, 'Thank you — your message has been received.');
}

$name = sanitize_text((string) ($fields['name'] ?? ''), 150);
$email = sanitize_text((string) ($fields['email'] ?? ''), 254);
$phone = sanitize_text((string) ($fields['phone'] ?? ''), 40);
$subject = sanitize_text((string) ($fields['subject'] ?? 'General Enquiry'), 200);
$message = sanitize_text((string) ($fields['message'] ?? ''), 5000);

$errors = [];
if ($name === '') $errors[] = 'name';
if (!is_valid_email($email)) $errors[] = 'email';
if ($message === '') $errors[] = 'message';

if ($errors !== []) {
    json_response(false, 'Please complete all required fields with valid information.', 422);
}

$companyEmail = env('COMPANY_EMAIL', 'info@hergerandco.com');

$safeName = e($name);
$safeEmail = e($email);
$safePhone = e($phone !== '' ? $phone : '—');
$safeSubject = e($subject);
$safeMessage = nl2br(e($message));

$internalHtml = <<<HTML
<h2>New Contact Form Submission</h2>
<p><strong>Name:</strong> {$safeName}</p>
<p><strong>Email:</strong> {$safeEmail}</p>
<p><strong>Phone:</strong> {$safePhone}</p>
<p><strong>Subject:</strong> {$safeSubject}</p>
<p><strong>Message:</strong></p>
<p>{$safeMessage}</p>
HTML;

[$sent, $err] = resend_send_email($companyEmail, 'Contact Form: ' . $subject, $internalHtml, $email);

if (!$sent) {
    json_response(false, $err ?? 'We could not send your message right now. Please try again shortly.', 502);
}

$confirmationHtml = <<<HTML
<h2>We've received your message</h2>
<p>Dear {$safeName},</p>
<p>Thank you for contacting Herger's &amp; Co. A member of our client relations team
will respond within one business day. For urgent matters, please call our office
directly during business hours.</p>
<p>Warm regards,<br/>Herger's &amp; Co.</p>
HTML;
resend_send_email($email, "We've received your message — Herger's & Co.", $confirmationHtml);

json_response(true, 'Thank you — your message has been sent. We will respond within one business day.');
