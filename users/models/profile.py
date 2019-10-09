from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, verbose_name='User description', null=True)
    birth_date = models.DateField(verbose_name='Birth date', null=True)
    birth_place = models.CharField(max_length=75, verbose_name='Birth place', null=True)
    image_user = models.URLField(max_length=300, verbose_name='User Picture', null=True, blank=True)

    def __str__(self):
        return self.user.username
