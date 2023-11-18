#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install git+https://github.com/benoitc/gunicorn.git
export PATH=$PATH:/usr/local/python3/bin
pip install gunicorn==20.1.0
python manage.py collectstatic --no-input
python manage.py migrate