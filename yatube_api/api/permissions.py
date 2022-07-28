from rest_framework import permissions


class IsAuthorOnly(permissions.BasePermission):

    message = 'You are not an author:('

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
