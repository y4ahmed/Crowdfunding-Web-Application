from django.views.decorators.csrf import csrf_protect
from django.shortcuts import (
    # render_to_response,
    render
)
# from django.contrib.auth.models import User

# from groups.forms import *
# from frontend.models import BaseUser
# from groups.models import Group


@csrf_protect
def manage_site(request):
    return render(request, 'site_manager/manage_site.html')


def give_site_manager_role(request):
    # TODO: Allow Site Manager to add Site Manager role to user
    return


def suspend_user(request):
    # TODO: Allow Site Manager to suspend a user's acess to their account
    return


def restore_user(request):
    # TODO: Allow Site Manager to restore a user's acecss to their account
    return


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
