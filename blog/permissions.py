from rest_framework import permissions


class BlogEntryPermission(permissions.BasePermission):
    message = 'you are not owner this entry'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author_id == request.user.id
