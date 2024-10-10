from rest_framework import permissions

class OnlyForOneUser(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        # print('USER', user)
        return user.username == 'admin'
