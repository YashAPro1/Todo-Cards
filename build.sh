#!/usr/bin/env bash
# exit on error
set -o errexit
echo $PATH
export PATH=$PATH:/opt/render/.local/bin
pip install -r requirements.txt

echo "Hi"
echo $PATH

python manage.py collectstatic --no-input
python manage.py migrate
pip install gunicorn==20.1.0
gunicorn --bind 127.0.0.1:8080 djangoapi.wsgi:application

