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

$name = sanitize_text((string) ($fields['first_name'] ?? '') . ' ' . (string) ($fields['last_name'] ?? ''), 150);
$firstName = sanitize_text((string) ($fields['first_name'] ?? ''), 100);
$lastName = sanitize_text((string) ($fields['last_name'] ?? ''), 100);
$email = sanitize_text((string) ($fields['email'] ?? ''), 254);
$phone = sanitize_text((string) ($fields['phone'] ?? ''), 40);
$company = sanitize_text((string) ($fields['company'] ?? ''), 150);
$role = sanitize_text((string) ($fields['role'] ?? ''), 150);
$officeAddress = sanitize_text((string) ($fields['office_address'] ?? ''), 250);
$residentialAddress = sanitize_text((string) ($fields['residential_address'] ?? ''), 250);
$lga = sanitize_text((string) ($fields['lga'] ?? ''), 100);
$state = sanitize_text((string) ($fields['state'] ?? ''), 100);
$country = sanitize_text((string) ($fields['country'] ?? ''), 100);
$subject = sanitize_text((string) ($fields['subject'] ?? 'General Enquiry'), 200);
$message = sanitize_text((string) ($fields['message'] ?? ''), 5000);

$errors = [];
if ($firstName === '') $errors[] = 'first_name';
if ($lastName === '') $errors[] = 'last_name';
if (!is_valid_email($email)) $errors[] = 'email';
if ($phone === '') $errors[] = 'phone';
if ($message === '') $errors[] = 'message';

if ($errors !== []) {
    json_response(false, 'Please complete all required fields with valid information.', 422);
}

$companyEmail = env('COMPANY_EMAIL', 'info@hergerandco.com');

$safeName = e($name);
$safeEmail = e($email);
$safePhone = e($phone);
$safeCompany = e($company !== '' ? $company : '—');
$safeRole = e($role !== '' ? $role : '—');
$safeOfficeAddress = e($officeAddress !== '' ? $officeAddress : '—');
$safeResidentialAddress = e($residentialAddress !== '' ? $residentialAddress : '—');
$safeLga = e($lga !== '' ? $lga : '—');
$safeState = e($state !== '' ? $state : '—');
$safeCountry = e($country !== '' ? $country : '—');
$safeSubject = e($subject);
$safeMessage = nl2br(e($message));

$internalHtml = <<<HTML
<h2>New Contact Form Submission</h2>
<p><strong>Name:</strong> {$safeName}</p>
<p><strong>Official Email:</strong> {$safeEmail}</p>
<p><strong>Phone:</strong> {$safePhone}</p>
<p><strong>Company / Business:</strong> {$safeCompany}</p>
<p><strong>Leadership Position / Role:</strong> {$safeRole}</p>
<p><strong>Office Address:</strong> {$safeOfficeAddress}</p>
<p><strong>Residential Address:</strong> {$safeResidentialAddress}</p>
<p><strong>County / L.G.A:</strong> {$safeLga}</p>
<p><strong>State / Province:</strong> {$safeState}</p>
<p><strong>Country:</strong> {$safeCountry}</p>
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
