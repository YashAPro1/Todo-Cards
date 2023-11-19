#!/usr/bin/env bash
# exit on error
set -o errexit
echo $PATH
export PATH=$PATH:/opt/render/.local/bin
pip install -r requirements.txt

echo "Hi"
echo $PATH
pip install gunicorn==20.1.0
echo $PATH

python manage.py collectstatic --no-input
python manage.py migrate
cd /opt/render/.local/bin