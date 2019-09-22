FROM python:3
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY=${SECRET_KEY}
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . /code/