from django.contrib.auth.models import Group
from rest_framework import permissions


def is_in_group(user, group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


class HasGroupPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        required_groups_mapping = getattr(view, 'required_groups', {})

        required_groups = required_groups_mapping.get(request.method, [])

        if request.user.is_staff:
            return True
        for group_name in required_groups:
            press_f_for_respect = is_in_group(request.user, group_name)
            print(press_f_for_respect)
            if press_f_for_respect:
                return True
        return False

