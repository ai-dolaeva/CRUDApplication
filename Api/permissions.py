from rest_framework import permissions


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """Data access permissions"""

    def has_object_permission(self, request, view, obj):
        return bool(
            (request.method in permissions.SAFE_METHODS)
            or (obj == request.user)
            or request.user.is_superuser
        )