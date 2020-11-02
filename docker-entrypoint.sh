#!/bin/bash

# Install requeriments
pip install -r /var/www/html/etitango/requirements.txt

# Collect static files
# echo "===============Collect static files==============="
# python3 /var/www/html/etitango/manage.py collectstatic --noinput

# Apply database migrations
echo "===============Apply database migrations==============="
python3 /var/www/html/etitango/manage.py makemigrations profiles blog pages events expenditure countries
python3 /var/www/html/etitango/manage.py migrate countries --fake
python3 /var/www/html/etitango/manage.py migrate

# Start server
echo "===============Starting server==============="
python3 /var/www/html/etitango/manage.py runserver 0.0.0.0:8000
# python3 /var/www/html/etitango/manage.py test apps.profiles.tests.test_forms
