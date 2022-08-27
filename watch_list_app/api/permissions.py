from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method == permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)

        # user_permission = bool(request.user and request.user.is_staff)
        # return request.method == "GET" or user_permission


class ReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user == obj.reviewer
