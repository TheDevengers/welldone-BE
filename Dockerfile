FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /django-project
COPY . /django-project/
WORKDIR /django-project
RUN /bin/bash -c 'source main/.env' && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python manage.py migrate --noinput
EXPOSE 8000
CMD ./run.sh