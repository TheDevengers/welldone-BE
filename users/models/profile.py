from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, verbose_name='User description')
    birthdate = models.DateField(verbose_name='Birthdate', null=True)
    birth_place = models.CharField(max_length=75, verbose_name='Birth place')

    def __str__(self):
        return self.user_id.username
