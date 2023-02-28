from rest_framework import permissions

from user_directory.models import Users


class IsOwnerOrAdmin(permissions.BasePermission):
    message = "ПОРОШОК УХОДИ"

    def has_object_permission(self, request, view, obj):
        if request.user.role in [Users.ADMIN, Users.MODERATOR] or request.user == obj.user:
            return True
        return False