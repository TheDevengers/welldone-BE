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