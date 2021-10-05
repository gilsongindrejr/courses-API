from rest_framework import permissions


class AuthenticatedReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            if request.user.is_authenticated:
                return True
            return False
        return False


class AuthenticatedPostOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            if request.user.is_authenticated:
                return True
            return False
        if request.method == 'GET':
            if request.user.is_authenticated:
                return True
        return False
