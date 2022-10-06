#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py migrate
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
python manage.py seed_data
python manage.py collectstatic --no-input
uvicorn stg_djangocon.asgi:application --host 0.0.0.0 --reload --reload-include '*.py,*.html,*.css'
