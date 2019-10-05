from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        from users.api import UserAPI
        # users/pk (GET, PUT, DELETE): admin or the self user
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and isinstance(view, UserAPI)

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user == obj
