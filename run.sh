#! /bin/bash

#source /code/main/.env
#yes | python manage.py makemigrations --merge
#python manage.py migrate --noinput
#python manage.py runserver 0.0.0.0:8000


pip install --upgrade pip && \
pip install -r requirements.txt && \
python manage.py collectstatic --noinput && \
python manage.py migrate --noinput && \
#gunicorn -w 4 -t 180 -b 0.0.0.0:8000 --capture-output --error-logfile - --log-file - project.wsgi
python manage.py runserver 0.0.0.0:8000