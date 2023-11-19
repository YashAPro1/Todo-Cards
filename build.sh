#!/usr/bin/env bash
# exit on error
set -o errexit
echo $PATH
export PATH=$PATH:/opt/render/.local/bin
export PATH=$PATH:/usr/local/python3/bin
pip install -r requirements.txt

echo "Hi"
echo $PATH
pip install gunicorn==20.1.0
echo $PATH

python manage.py collectstatic --no-input
python manage.py migrate
cd /usr/local/python3/bin
gunicorn app:app