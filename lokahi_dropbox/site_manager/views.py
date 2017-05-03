from django.views.decorators.csrf import csrf_protect
from django.shortcuts import (
    # render_to_response,
    render
)
from django.contrib.auth.models import User

from frontend.models import BaseUser
# from groups.forms import *
# from groups.models import Group


# This is not a view, just a method to abstract out stuff
def get_user_info(request):
    # Create basic user info container
    user_info = []
    # Populate user information container
    users = User.objects.all()
    for user in users:
        base_user = BaseUser.objects.get(user=user.pk)
        user_info.append({
            'pk': user.pk,
            'username': user.username,
            'email': user.email,
            'role': base_user.user_role,
        })
    return user_info


def give_site_manager_role(pk):
    base_user = BaseUser.objects.get(pk=pk)
    base_user.user_role = 'Site Manager'
    base_user.save()
    return True


def suspend_user(pk):
    base_user = BaseUser.objects.get(pk=pk)
    if base_user.user_role.find('_') == -1:
        base_user.user_role = 'Banned User_%s' % base_user.user_role
        base_user.save()
    return True


def restore_user(pk):
    base_user = BaseUser.objects.get(pk=pk)
    if base_user.user_role.find('_') != -1:
        base_user.user_role = base_user.user_role.split('_')[1]
        base_user.save()
    return True


@csrf_protect
def user_management(request):
    # Check if method is POST and apply appropriate action
    if request.method == 'POST':
        action = request.POST.get('action')
        pk = request.POST.get('pk')
        if action == 'suspend':
            suspend_user(pk)
        elif action == 'restore':
            restore_user(pk)
        else:
            give_site_manager_role(pk)

    base = BaseUser.objects.get(user=request.user)
    user_info = get_user_info(request)
    return render(
        request,
        'site_manager/user_management.html',
        {'user_info': user_info, 'type': base.user_role}
    )


# The below might just be handled by editing how groups render...
def add_user_to_group(request):
    # TODO: Allow Site Manager to add any user to any group
    return


def remove_user_from_group(request):
    # TODO: Allow Site Manager to remove any user from a group
    return


# The below things may just be handled by editing how the reports render...
def access_report(request):
    # TODO: Allow Site Manager to view any report
    return


def edit_report(request):
    # TODO: Allow Site Manager to edit any report
    return


def delete_report(request):
    # TODO: Allow Site Manager to delete any report
    return
