from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from groups.forms import *
from django.contrib.auth.models import User

# Create your views here.
@csrf_protect
def groups(request):
    return render(request, 'group/groups.html',)

def create_group(request):
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

            report_list = report_list_temp.split(",")

            is_duplicate = len(Group.objects.filter(group_name=group_name))

            if is_duplicate > 0:
                # TODO : raise error !
                # a group with this name already exists
                raise Error("group duplicate")

            group = Group.objects.create(group_name=group_name)

            for m in member_list:
                try:
                    user = User.objects.get(username__iexact=m)
                    base_user = BaseUser.objects.get(user=user)
                    group.member_list.add(base_user)
                except User.DoesNotExist:
                    # TODO: fix the error page redirection
                    raise forms.ValidationError(_('Invalid receiver name. Try again.'), code='invalid')

            # group.add_members(member_list)
            # group.add_reports(report_list)

            base_user = BaseUser.objects.get(user=request.user)
            groups = Group.objects.filter(member_list=base_user)

        return render(request, 'group/view_group.html', {'groups':groups})
    else:
        return render(request, 'group/create_group.html',)

def view_group(request):
    base_user = BaseUser.objects.get(user=request.user)
    groups = Group.objects.filter(member_list=base_user)
    return render(request, 'group/view_group.html', {'groups':groups})

def edit_group(request):
    if request.method == 'POST':
        form = EditGroupForm(data=request.POST)
        if form.is_valid():
            g = Group.objects.get(id=form.cleaned_data['group_id'])
            member_list = g.member_list.all()
            return render(request, 'group/each_group.html', {'group_name':g.group_name, 'members':member_list, 'group_id':g.id})

def add_members(request):
    if request.method == 'POST':
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
                    is_duplicate_user = len(Group.objects.filter(id=group.id, member_list=base_user))

                    if is_duplicate_user > 0:
                        # TODO: fix the error page redirection
                        raise Error("user" + user.username + "is already a member of the group")

                    group.member_list.add(base_user)
                except User.DoesNotExist:
                    # TODO: fix the error page redirection
                    raise forms.ValidationError(_('Invalid receiver name. Try again.'), code='invalid')


            return render(request, 'group/each_group.html', {'group_name':group.group_name, 'members':group.member_list.all(), 'group_id':group.id})
