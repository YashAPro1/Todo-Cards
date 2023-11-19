#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install git+https://github.com/benoitc/gunicorn.git
pip install gunicorn==20.1.0
echo $PATH
export PATH=$PATH:/opt/render/.local/bin
echo "Hi"
echo $PATH
python manage.py collectstatic --no-input
python manage.py migrate