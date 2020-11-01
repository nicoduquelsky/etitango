#!/bin/sh

set -e

# Collect static files
echo "===============Collect static files==============="
python manage.py collectstatic --noinput

# Apply database migrations
echo "===============Apply database migrations==============="
python manage.py makemigrations profiles blog pages events expenditure countries
python manage.py migrate countries --fake
python manage.py migrate

# Start server
echo "===============Starting server==============="
gunicorn etitango.wsgi:application --bind :8000
