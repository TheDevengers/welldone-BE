from django.db import models
from django.contrib.auth.models import User

class Follower(models.Model):
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE)
    followed_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.follower_id.username + '->' + self.followed_id.username
    