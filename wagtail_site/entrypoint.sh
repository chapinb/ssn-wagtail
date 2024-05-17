#!/usr/bin/env sh
set -e

poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate

# For Production:
poetry run gunicorn wagtail_site.wsgi:application --bind=0.0.0.0:8000 --access-logfile=-
