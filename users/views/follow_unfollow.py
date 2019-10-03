from django.shortcuts import redirect
from django.views import View

from users.controllers import FollowersController


class FollowView(View):
    def post(self, request, username=None):
        if request.user.is_authenticated:
            FollowersController.follow(request=request, username=username)
        return redirect(request.headers.get('referer'))


class UnfollowView(View):
    def post(self, request, username=None):
        if request.user.is_authenticated:
            FollowersController.unfollow(request=request, username=username)
        return redirect(request.headers.get('referer'))