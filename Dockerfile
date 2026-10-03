# Serves the pre-built frontend/ and proxies /api/*.php to backend/api/ via
# router.php — same setup as local dev (php -S ... -t frontend router.php).
FROM php:8.3-cli-alpine

RUN apk add --no-cache curl-dev oniguruma-dev \
    && docker-php-ext-install curl mbstring \
    && apk del curl-dev oniguruma-dev

WORKDIR /app
COPY . .

# Railway injects $PORT at runtime; default 8080 for local `docker run`.
CMD ["sh", "-c", "php -S 0.0.0.0:${PORT:-8080} -t frontend router.php"]
