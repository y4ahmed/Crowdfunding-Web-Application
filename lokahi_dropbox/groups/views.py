from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.contrib.auth.models import User

from groups.forms import (
    GroupForm, EditGroupForm, AddMembersForm, ExitGroupForm)
from frontend.models import BaseUser
from groups.models import Group

from reports.models import Report

from django.http import HttpResponseRedirect


@csrf_protect
def groups(request):
    base = BaseUser.objects.get(user=request.user)
    return render(request, 'group/groups.html', {'type': base.user_role})


def create_group(request):
    base = BaseUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            member_list_temp = form.cleaned_data['member_list']
            report_list_temp = form.cleaned_data['report_list']
            member_list = []
            member_list_temp = member_list_temp.split(",")
            for mem in member_list_temp:
                member_list += [mem.strip()]
            member_list = member_list + [request.user.username]

            report_list = []
            report_list_temp = report_list_temp.split(",")
            for r in report_list_temp:
                report_list += [r.strip()]

            is_duplicate = len(Group.objects.filter(group_name=group_name))

            if is_duplicate > 0:
                # a group with this name already exists
                return render(
                    request,
                    'group/create_group.html',
                    {'duplicate_name': True, 'type': base.user_role}
                )
                # raise Error("group duplicate, group names must be unique")

            base_user_list = []
            report_obj_list = []

            for m in member_list:
                try:
                    user = User.objects.get(username__iexact=m)
                    base_user = BaseUser.objects.get(user=user)
                    print("adding ", m)
                    base_user_list += [base_user]
                except User.DoesNotExist:
                    return render(
                        request,
                        'group/create_group.html',
                        {'invalid_user': True, 'type': base.user_role,
                         'invalid_name': m},
                    )
                    # raise forms.ValidationError(_('Invalid receiver name. Try again.'), code='invalid')

            users_private_reports = Report.objects.filter(
                owner_id=request.user, private=True)

            if len(users_private_reports) == 0:
                return render(
                    request,
                    'group/create_group.html',
                    {'no_reports': True, 'type': base.user_role}
                )

            for r in report_list:
                try:
                    # print(r)
                    # pass in a list of report objects, and return the object
                    # with the matching name
                    report_obj = find_report(users_private_reports, r)
                    # print(report_obj)

                    if report_obj is None:
                        return render(
                            request,
                            'group/create_group.html',
                            {
                                'invalid_private_report_name': True,
                                'invalid_report_private': r,
                                'type': base.user_role
                            }
                        )

                    report_obj_list += [report_obj]
                except Report.DoesNotExist:
                    return render(
                        request,
                        'group/create_group.html',
                        {
                            'invalid_report': True,
                            'invalid_report_name': r,
                            'type': base.user_role
                        },
                    )

            group = Group.objects.create(group_name=group_name)

            for o in base_user_list:
                group.member_list.add(o)

            # add every report to the groups model
            for o in report_obj_list:
                group.report_list.add(o)

            # add every user other than the current one to each report
            for o in base_user_list:
                if not o.user == request.user:
                    for r in report_obj_list:
                        o.reports.add(r)

            # group.save()

            # print(group.member_list.all())

            # print(len(group.report_list.all()))

            base_user = BaseUser.objects.get(user=request.user)
            groups = Group.objects.filter(member_list=base_user)
            return render(
                request,
                'group/view_group.html',
                {'groups': groups, 'type': base.user_role}
            )

        return render(
            request,
            'group/create_group.html',
            {'invalid_entry': True, 'type': base.user_role}
        )
    else:
        return render(
            request,
            'group/create_group.html',
            {'type': base.user_role}
        )


def find_report(list_reports, report_name):
    for report in list_reports:
        if report.title == report_name:
            return report
    return None


def view_group(request):
    base_user = BaseUser.objects.get(user=request.user)
    groups = Group.objects.filter(member_list=base_user)
    return render(
        request,
        'group/view_group.html',
        {'groups': groups, 'type': base_user.user_role}
    )


def edit_group(request):
    base_user = BaseUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditGroupForm(data=request.POST)
        if form.is_valid():
            g = Group.objects.get(id=form.cleaned_data['group_id'])
            member_list = g.member_list.all()
            return render(
                request,
                'group/each_group.html',
                {
                    'reports': g.report_list.all(),
                    'group_name': g.group_name,
                    'members': member_list,
                    'group_id': g.id,
                    'username': request.user.username,
                    'type': base_user.user_role
                }
            )


def add_members(request):
    base = BaseUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = ExitGroupForm(data=request.POST)
        if form.is_valid():
            user = User.objects.get(
                username__iexact=form.cleaned_data['username'])
            base_user = BaseUser.objects.get(user=user)
            group = Group.objects.get(id=form.cleaned_data['group_id'])

            group.member_list.remove(base_user)

            groups = Group.objects.filter(member_list=base_user)
            return render(request, 'group/view_group.html', {'groups': groups})

        form = AddMembersForm(data=request.POST)
        if form.is_valid():
            temp_list = form.cleaned_data['new_members']
            group_id = form.cleaned_data['group_id']
            temp_list = temp_list.split(',')
            member_list = []
            for m in temp_list:
                member_list += [m.strip()]

            group = Group.objects.get(id=group_id)

            for m in member_list:
                try:
                    user = User.objects.get(username__iexact=m)
                    base_user = BaseUser.objects.get(user=user)
                    is_duplicate_user = len(Group.objects.filter(
                        id=group.id, member_list=base_user))

                    if is_duplicate_user > 0:
                        return render(
                            request,
                            'group/each_group.html',
                            {
                                'reports': group.report_list.all(),
                                'group_name': group.group_name,
                                'members': group.member_list.all(),
                                'group_id': group.id,
                                'username': request.user.username,
                                'is_duplicate': True,
                                'duplicate_name': m,
                                'type': base.user_role
                            }
                        )
                        # raise Error("user" + user.username + "is already a member of the group")

                    group.member_list.add(base_user)
                except User.DoesNotExist:
                    return render(
                        request,
                        'group/each_group.html',
                        {
                            'reports': group.report_list.all(),
                            'group_name': group.group_name,
                            'members': group.member_list.all(),
                            'group_id': group.id,
                            'username': request.user.username,
                            'is_invalid': True,
                            'invalid_name': m,
                            'type': base.user_role
                        }
                    )
                    # raise forms.ValidationError(_('Invalid receiver name. Try again.'), code='invalid')

            return render(
                request, 'group/each_group.html',
                {
                    'reports': group.report_list.all(),
                    'group_name': group.group_name,
                    'members': group.member_list.all(),
                    'group_id': group.id,
                    'username': request.user.username,
                    'type': base.user_role
                }
            )
        return HttpResponseRedirect('/groups/view_groups')
