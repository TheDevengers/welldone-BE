# WELLDONE

## Python version
We use 3.7.x to create this project. Probably works with some older versions as well, but is not tested.

## How to clone this repo

1. Create a virtual environment and activate it, the way you like. Below you can find some ways, they are not unique, but they can help.
2. Install all dependencies using ```pip install -r requirements.txt```
3. Create a copy of ```.env.example``` file and change the name to ```.env```
4. Create a migration of the applications ```python manage.py migrate```
5. Create a superuser ```python manage.py createsuperuser``` f.e.: suadmin@PompeuFabra-2019
6. Run dev server: `python manage.py runserver`


## Create and activate virtual environments. 
You must have installed Python on your system. Create a virtualenv in your folder using tools as you like. In this examples we choose ```env``` as folder name.
```virtualenv env```
```pyvenv env```

After the creation you should have a ```env``` folder in your workspace, you should activate it.
MAC: ```source bin/activate```
WIN(cmd, PS): ```env\Scripts\activate```
WIN(bash): ```source env/Scripts/activate```

The virtual environment is activated when the prompt has the virtualenv name inside parenthesis.

For configure it in Visual Studio Code follow this: https://code.visualstudio.com/docs/python/tutorial-django

## Send Mails
We use Sendgrid service to send emails. There are limit of 100 Emails per day, so use it wisely.
The system uses the API connection so new librery must to be installed in teh system, look at requirements.txt.
The way to send an email is easy:
```
from main.notifier.mail import SendMail

SendMail.send_no_reply_email(to_emails='mail address',
                             subject='mail subject',
                             content='content of mail, can be html') 
```

## Build and run your app with Compose

First: Donwload [docker]('https://www.docker.com/products/docker-desktop'), also as a complement you can download [kitematic]('https://kitematic.com/') to use Docker more graphic.

[Instalation]('https://docs.docker.com/compose/install/#install-compose') guide.


Run `docker-compose up -d` and Compose starts and runs your entire app:

`-d: Detached mode: Run container in the background, print new container name.`


Open http://localhost:8000 to view it in the browser.

INFO:
 - docker-compose up: It instructs Docker to create the container, and execute it according to docker-compose.yml
 - docker-compose down: It turns off all the services you raised with docker-compose up
 - docker-compose ps: This allows you to see the containers running.

DOC: [docker-compose cheatsheet]('https://devhints.io/docker-compose')

## API

Request to http://localhost:8000/api/v1

### Authentication

For more info: https://github.com/davesque/django-rest-framework-simplejwt
```
POST /token/             To get access and refresh token
POST /token/refresh/     To get access token from refresh token
```

### Articles

```
GET     /articles           Authenticated users get own list article
POST    /articles           Authenticated users create article as author
PUT     /articles/<pk>      Authenticated users modify entire own articles
PATCH   /articles/<pk>      Authenticated users modify partiallly own articles
DELETE  /articles/<pk>      Authenticated users delete own articles

GET /categories         Get list of categories
```