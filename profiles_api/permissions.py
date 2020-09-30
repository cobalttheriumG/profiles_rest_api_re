from rest_framework import permissions


class UserProfilePermission(permissions.BasePermission):
    """Set User profile permission"""

    def has_object_permission(self, request, view, obj):
        """set user permission to put, patch, and delete object"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return  obj.id == request.user.id