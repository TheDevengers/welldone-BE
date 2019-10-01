#! /bin/bash

#gunicorn -w 4 -t 180 -b 0.0.0.0:8000 --capture-output --error-logfile - --log-file - project.wsgi
python manage.py runserver 0.0.0.0:8000