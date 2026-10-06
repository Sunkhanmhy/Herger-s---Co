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
$altPhone = sanitize_text((string) ($fields['alt_phone'] ?? ''), 40);
$company = sanitize_text((string) ($fields['company'] ?? ''), 150);
$practiceArea = sanitize_text((string) ($fields['practice_area'] ?? 'General Enquiry'), 150);
$officeAddress = sanitize_text((string) ($fields['office_address'] ?? ''), 250);
$residentialAddress = sanitize_text((string) ($fields['residential_address'] ?? ''), 250);
$caseType = sanitize_text((string) ($fields['case_type'] ?? ''), 200);
$opposingParty = sanitize_text((string) ($fields['opposing_party'] ?? ''), 200);
$priorCounsel = sanitize_text((string) ($fields['prior_counsel'] ?? 'No'), 10);
$urgency = sanitize_text((string) ($fields['urgency'] ?? 'Standard'), 30);
$contactMethod = sanitize_text((string) ($fields['contact_method'] ?? 'Email'), 30);
$preferredDate = sanitize_text((string) ($fields['preferred_date'] ?? ''), 20);
$preferredTime = sanitize_text((string) ($fields['preferred_time'] ?? ''), 20);
$referralSource = sanitize_text((string) ($fields['referral_source'] ?? ''), 150);
$notes = sanitize_text((string) ($fields['notes'] ?? ''), 3000);
$consent = trim((string) ($fields['consent'] ?? ''));

$errors = [];
if ($name === '') $errors[] = 'name';
if (!is_valid_email($email)) $errors[] = 'email';
if ($phone === '') $errors[] = 'phone';
if ($notes === '') $errors[] = 'notes';
if ($consent === '') $errors[] = 'consent';

if ($errors !== []) {
    json_response(false, 'Please complete all required fields, including the confidentiality acknowledgement.', 422);
}

$companyEmail = env('COMPANY_EMAIL', 'info@hergerandco.com');
$calendlyUrl = env('CALENDLY_URL', 'https://calendly.com/hergerandco/free-consultation');

$safeName = e($name);
$safeEmail = e($email);
$safePhone = e($phone);
$safeAltPhone = e($altPhone !== '' ? $altPhone : '—');
$safeCompany = e($company !== '' ? $company : '—');
$safePracticeArea = e($practiceArea);
$safeOfficeAddress = e($officeAddress !== '' ? $officeAddress : '—');
$safeResidentialAddress = e($residentialAddress !== '' ? $residentialAddress : '—');
$safeCaseType = e($caseType !== '' ? $caseType : '—');
$safeOpposingParty = e($opposingParty !== '' ? $opposingParty : '—');
$safePriorCounsel = e($priorCounsel);
$safeUrgency = e($urgency);
$safeContactMethod = e($contactMethod);
$safePreferredDate = e($preferredDate !== '' ? $preferredDate : '—');
$safePreferredTime = e($preferredTime !== '' ? $preferredTime : '—');
$safeReferralSource = e($referralSource !== '' ? $referralSource : '—');
$safeNotes = nl2br(e($notes));
$safeCalendlyUrl = e($calendlyUrl);

$internalHtml = <<<HTML
<h2>New Free Consultation Request</h2>
<p><strong>Name:</strong> {$safeName}</p>
<p><strong>Official Email:</strong> {$safeEmail}</p>
<p><strong>Phone:</strong> {$safePhone}</p>
<p><strong>Alternate Phone:</strong> {$safeAltPhone}</p>
<p><strong>Company / Organization:</strong> {$safeCompany}</p>
<p><strong>Office Address:</strong> {$safeOfficeAddress}</p>
<p><strong>Residential Address:</strong> {$safeResidentialAddress}</p>
<p><strong>Practice Area:</strong> {$safePracticeArea}</p>
<p><strong>Matter / Case Type:</strong> {$safeCaseType}</p>
<p><strong>Opposing Party:</strong> {$safeOpposingParty}</p>
<p><strong>Previously Consulted Another Lawyer/Firm:</strong> {$safePriorCounsel}</p>
<p><strong>Urgency Level:</strong> {$safeUrgency}</p>
<p><strong>Preferred Contact Method:</strong> {$safeContactMethod}</p>
<p><strong>Preferred Consultation Date:</strong> {$safePreferredDate}</p>
<p><strong>Preferred Consultation Time:</strong> {$safePreferredTime}</p>
<p><strong>How They Heard About Us:</strong> {$safeReferralSource}</p>
<p><strong>Case Summary / Background:</strong></p>
<p>{$safeNotes}</p>
HTML;

[$sent, $err] = resend_send_email($companyEmail, 'Free Consultation Request: ' . $practiceArea, $internalHtml, $email);

if (!$sent) {
    json_response(false, $err ?? 'We could not submit your request right now. Please try again shortly.', 502);
}

$confirmationHtml = <<<HTML
<h2>Your free consultation request has been received</h2>
<p>Dear {$safeName},</p>
<p>Thank you for requesting a complimentary consultation with Herger's &amp; Co. regarding
<strong>{$safePracticeArea}</strong>. A member of our team will contact you via your preferred
method to confirm a convenient time.</p>
<p>If you would prefer to book a slot directly on our live calendar instead, you may do so here:</p>
<p><a href="{$safeCalendlyUrl}" target="_blank" rel="noopener">Book your free consultation slot</a></p>
<p>Please note this initial consultation does not create an attorney-client relationship;
this is only established once engagement terms have been confirmed in writing.</p>
<p>We look forward to speaking with you.</p>
<p>Warm regards,<br/>Herger's &amp; Co.</p>
HTML;
resend_send_email($email, 'Your consultation request — Herger\'s & Co.', $confirmationHtml);

json_response(true, 'Thank you — your consultation request has been sent. Our team will contact you shortly to confirm a time, and a confirmation has been emailed to you.');
