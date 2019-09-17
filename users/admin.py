from django.contrib import admin
from users.models import Favorite, Follower, Profile

admin.site.register(Favorite)
admin.site.register(Follower)
admin.site.register(Profile)
