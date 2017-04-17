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

            member_list = member_list_temp.split(",")
            member_list = member_list + [request.user.username]
            report_list = report_list_temp.split(",")

            # form.validate_members(member_list)

            group = Group.objects.create(group_name=group_name)
            group.add_members(member_list)


        return render(request, 'group/view_group.html',)
    else:
        return render(request, 'group/create_group.html',)

def view_group(request):
    return render(request, 'group/view_group.html',)
