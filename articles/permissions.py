from rest_framework.permissions import BasePermission


class ArticlePermission(BasePermission):

    def has_permission(self, request, view):
        # articles (GET): user authenticated
        # articles (POST): user authenticated
        # articles/pk (GET): user authenticated
        # articles/pk (PUT): user authenticated
        # articles/pk (DELETE): user authenticated
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class FavoritePermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user