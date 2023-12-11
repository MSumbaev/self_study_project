from rest_framework.permissions import BasePermission


class IsNotModerator(BasePermission):
    """Ограничение - для юзеров не входящих в группу модераторов"""
    def has_permission(self, request, view):
        return not request.user.groups.filter(name='moderator')


class IsModerator(BasePermission):
    """Ограничение - для юзеров входящих в группу модераторов"""
    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator'):
            return True
        return False


class IsTeacher(BasePermission):
    """Ограничение - для юзеров входящих в группу 'teacher'"""
    def has_permission(self, request, view):
        if request.user.groups.filter(name='teacher'):
            return True
        return False


class IsOwner(BasePermission):
    """Ограничение - для юзеров работающих с собственными объектами"""
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False
