from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, render
from search.forms import *
from django.contrib.auth.models import User
from frontend.models import *

# Create your views here.


@csrf_exempt
def basic_search(request):
    if request.method == "POST":
        form = BasicSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            reports = Report.objects.filter(owner_id=request.user).filter(title__icontains=search)
            for report in reports:
                print(report.title)
            return render(request, 'group/groups.html', {})
