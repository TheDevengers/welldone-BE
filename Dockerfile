FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-project
COPY . /django-project/
WORKDIR /django-project
RUN /bin/bash -c 'source main/.env'
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN python manage.py collectstatic --noinput
RUN python manage.py migrate --noinput
EXPOSE 8000
CMD ./run.sh