from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from search.forms import *
from django.contrib.auth.models import User
from frontend.models import *

# Create your views here.
@csrf_protect
def basic_search(request):
    if request.method == "POST":
        form = BasicSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            base_user = BaseUser.objects.get(user=request.user)
            reports = base_user.reports.all().filter(title__icontains=search)
            return render(request, 'group/groups.html',)
