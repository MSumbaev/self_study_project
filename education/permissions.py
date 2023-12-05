from rest_framework.permissions import BasePermission


class IsNotModerator(BasePermission):

    def has_permission(self, request, view):
        return not request.user.groups.filter(name='moderator')


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator'):
            return True
        return False


class IsTeacher(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='teacher'):
            return True
        return False


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
