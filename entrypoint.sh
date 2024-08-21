#!/bin/ash

echo "Apply database migrations"
python manage.py makemigrations && python3 manage.py migrate --noinput && python3 manage.py collectstatic --noinput

exec "$@"
