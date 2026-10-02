<?php
/**
 * Local dev router for PHP's built-in server, needed now that frontend/ and
 * backend/ are separate folders. Run from the project root:
 *
 *   php -S localhost:8000 -t frontend router.php
 *
 * Static files are served from frontend/ (the -t docroot) as normal; any
 * request path starting with /api/ is instead resolved against backend/api/
 * so the browser-facing URLs (e.g. "api/contact.php") keep working unchanged.
 */
declare(strict_types=1);

$uri = parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH);
$uri = $uri === null ? '/' : rawurldecode($uri);

if (str_starts_with($uri, '/api/')) {
    $file = __DIR__ . '/backend' . $uri;
    if (is_file($file)) {
        chdir(dirname($file));
        require $file;
        return true;
    }
    http_response_code(404);
    return true;
}

return false; // let the built-in server serve the static file from the -t docroot
