#!/bin/sh

set -e

echo "=========================================="
echo "       Starting Pharmacy Application"
echo "=========================================="

echo "[1/2] Applying database migrations..."

python manage.py migrate --noinput

echo "[2/2] Database migrations completed."

echo "=========================================="
echo "Application is ready!"
echo "Please open your browser and visit:"
echo "http://localhost:8000"
echo "=========================================="

exec "$@"