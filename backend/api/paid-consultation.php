<?php
declare(strict_types=1);

require_once __DIR__ . '/lib/security.php';
require_once __DIR__ . '/lib/resend.php';

apply_cors_headers();
require_post_method();
enforce_rate_limit('paid_consultation', 6, 600);

$fields = $_POST;
if (is_honeypot_triggered($fields)) {
    json_response(true, 'Thank you — your paid consultation request has been received.');
}

$name = sanitize_text((string) ($fields['name'] ?? ''), 150);
$email = sanitize_text((string) ($fields['email'] ?? ''), 254);
$phone = sanitize_text((string) ($fields['phone'] ?? ''), 40);
$sessionType = sanitize_text((string) ($fields['session_type'] ?? ''), 150);
$hours = sanitize_text((string) ($fields['hours'] ?? ''), 10);
$urgency = sanitize_text((string) ($fields['urgency'] ?? 'standard'), 30);
$feeSummary = sanitize_text((string) ($fields['fee_summary'] ?? ''), 300);
$notes = sanitize_text((string) ($fields['notes'] ?? ''), 3000);

$errors = [];
if ($name === '') $errors[] = 'name';
if (!is_valid_email($email)) $errors[] = 'email';
if ($sessionType === '') $errors[] = 'session_type';

if ($errors !== []) {
    json_response(false, 'Please complete all required fields with valid information.', 422);
}

$companyEmail = env('COMPANY_EMAIL', 'info@hergerandco.com');

$safeName = e($name);
$safeEmail = e($email);
$safePhone = e($phone !== '' ? $phone : '—');
$safeSessionType = e($sessionType);
$safeHours = e($hours !== '' ? $hours : '—');
$safeUrgency = e($urgency);
$safeFeeSummary = e($feeSummary !== '' ? $feeSummary : '—');
$safeNotes = nl2br(e($notes !== '' ? $notes : '—'));

$internalHtml = <<<HTML
<h2>New Paid Consultation Booking Request</h2>
<p><strong>Name:</strong> {$safeName}</p>
<p><strong>Email:</strong> {$safeEmail}</p>
<p><strong>Phone:</strong> {$safePhone}</p>
<p><strong>Session Type:</strong> {$safeSessionType}</p>
<p><strong>Estimated Hours:</strong> {$safeHours}</p>
<p><strong>Urgency:</strong> {$safeUrgency}</p>
<p><strong>Client-side Fee Estimate:</strong> {$safeFeeSummary}</p>
<p><strong>Notes:</strong></p>
<p>{$safeNotes}</p>
<p><em>Note: this is a client-side estimate only. Final billing is confirmed in writing
by the firm's billing department before any invoice is raised.</em></p>
HTML;

[$sent, $err] = resend_send_email($companyEmail, 'Paid Consultation Request: ' . $sessionType, $internalHtml, $email);

if (!$sent) {
    json_response(false, $err ?? 'We could not submit your request right now. Please try again shortly.', 502);
}

$confirmationHtml = <<<HTML
<h2>Your paid consultation request has been received</h2>
<p>Dear {$safeName},</p>
<p>Thank you for requesting a paid consultation for <strong>{$safeSessionType}</strong>.
Your estimated fee, based on the details you provided, was:</p>
<p style="font-size:18px;font-weight:bold;">{$safeFeeSummary}</p>
<p>This figure is an estimate only. Our billing team will confirm the final scope and
fee in writing, and payment instructions will follow before your session is scheduled.</p>
<p>Warm regards,<br/>Herger's &amp; Co.</p>
HTML;
resend_send_email($email, 'Your paid consultation estimate — Herger\'s & Co.', $confirmationHtml);

json_response(true, 'Thank you — your request has been sent. Our billing team will confirm the final fee and next steps by email.');
