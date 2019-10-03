from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from users.models import Follower


class FollowersController(object):

    @staticmethod
    def follow(request, username):
        if request.user != username:
            follower = Follower()
            follower.follower = request.user
            followed = get_object_or_404(User, username=username)
            follower.followed = followed
            follower.save()

    @staticmethod
    def unfollow(request, username):
        follower_pk = get_object_or_404(User, username=request.user)
        followed_pk = get_object_or_404(User, username=username)
        follower = Follower.objects.filter(follower=follower_pk, followed=followed_pk)
        follower.delete()