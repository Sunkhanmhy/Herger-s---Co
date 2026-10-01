<?php
declare(strict_types=1);

require_once __DIR__ . '/lib/security.php';
require_once __DIR__ . '/lib/resend.php';

apply_cors_headers();
require_post_method();
enforce_rate_limit('consultation', 6, 600);

$fields = $_POST;
if (is_honeypot_triggered($fields)) {
    json_response(true, 'Thank you — we will be in touch to confirm your slot.');
}

$name = sanitize_text((string) ($fields['name'] ?? ''), 150);
$email = sanitize_text((string) ($fields['email'] ?? ''), 254);
$phone = sanitize_text((string) ($fields['phone'] ?? ''), 40);
$practiceArea = sanitize_text((string) ($fields['practice_area'] ?? 'General Enquiry'), 150);
$notes = sanitize_text((string) ($fields['notes'] ?? ''), 3000);
$preferredSlot = sanitize_text((string) ($fields['preferred_slot'] ?? ''), 200);

$errors = [];
if ($name === '') $errors[] = 'name';
if (!is_valid_email($email)) $errors[] = 'email';

if ($errors !== []) {
    json_response(false, 'Please provide your name and a valid email address.', 422);
}

$companyEmail = env('COMPANY_EMAIL', 'info@hergerandco.com');
$calendlyUrl = env('CALENDLY_URL', 'https://calendly.com/hergerandco/free-consultation');

$safeName = e($name);
$safeEmail = e($email);
$safePhone = e($phone !== '' ? $phone : '—');
$safePracticeArea = e($practiceArea);
$safeNotes = nl2br(e($notes !== '' ? $notes : '—'));
$safePreferredSlot = e($preferredSlot !== '' ? $preferredSlot : 'No preference specified — see Calendly booking');
$safeCalendlyUrl = e($calendlyUrl);

$internalHtml = <<<HTML
<h2>New Free Consultation Request</h2>
<p><strong>Name:</strong> {$safeName}</p>
<p><strong>Email:</strong> {$safeEmail}</p>
<p><strong>Phone:</strong> {$safePhone}</p>
<p><strong>Practice Area:</strong> {$safePracticeArea}</p>
<p><strong>Preferred Slot (from Calendly widget):</strong> {$safePreferredSlot}</p>
<p><strong>Notes:</strong></p>
<p>{$safeNotes}</p>
HTML;

[$sent, $err] = resend_send_email($companyEmail, 'Free Consultation Request: ' . $practiceArea, $internalHtml, $email);

if (!$sent) {
    json_response(false, $err ?? 'We could not submit your request right now. Please try again shortly.', 502);
}

$confirmationHtml = <<<HTML
<h2>Your free consultation request has been received</h2>
<p>Dear {$safeName},</p>
<p>Thank you for requesting a complimentary consultation with Herger &amp; Co. regarding
<strong>{$safePracticeArea}</strong>. Please use the link below to select a convenient time
on our live calendar if you have not already done so — your slot is only confirmed once
it appears on our calendar.</p>
<p><a href="{$safeCalendlyUrl}" target="_blank" rel="noopener">Book your free consultation slot</a></p>
<p>We look forward to speaking with you.</p>
<p>Warm regards,<br/>Herger's &amp; Co.</p>
HTML;
resend_send_email($email, 'Your consultation request — Herger\'s & Co.', $confirmationHtml);

json_response(true, 'Thank you — please confirm your preferred time on the calendar. A confirmation has been emailed to you.');
