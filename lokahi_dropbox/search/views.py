from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from search.forms import *
from django.contrib.auth.models import User
from frontend.models import *
from django.http import HttpResponseRedirect

# Create your views here.


@csrf_protect
def basic_search(request):
    if request.method == "POST":
        form = BasicSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            reports = Report.objects.filter(owner_id=request.user).filter(title__icontains=search)
            # TEST TODO remove
            for report in reports:
                print(report.title)
            return render(request, 'searches/advanced_search.html', {'form': AdvancedSearchForm()})

@csrf_protect
def advanced_search(request):
    if request.method == "POST":
        form = AdvancedSearchForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            company_name = form.cleaned_data['company_name']
            ceo = form.cleaned_data['ceo']
            location = form.cleaned_data['location']
            country = form.cleaned_data['country']
            sector = form.cleaned_data['sector']
            projects = form.cleaned_data['projects']
            time_created = form.cleaned_data['time_created']

            reports = [[], [], [], [], [], [], [], []]
            checks = [False, False, False, False, False, False, False, False]

            # all of the users reports
            all_reports = Report.objects.filter(owner_id=request.user)

            if title == "" and company_name == "" and ceo == "" and \
            location == "" and country == "" and sector == "" and projects == "" and time_created == "":
                print("here")
                return render(request, 'searches/advanced_search.html', {'empty_field': True, 'form': AdvancedSearchForm()})

            if not title == "":
                reports[0] = all_reports.filter(title__icontains=title)
                # print(reports[0])
            if not company_name == "":
                reports[1] = all_reports.filter(compName__icontains=company_name)
                # print(reports[1])
            if not ceo == "":
                reports[2] = all_reports.filter(ceo__icontains=ceo)
                # print(reports[2])
            if not location == "":
                reports[3] = all_reports.filter(location__icontains=location)
                # print(reports[3])
            if not country == "":
                reports[4] = all_reports.filter(country__icontains=country)
                # print(reports[4])
            if not sector == "":
                reports[5] = all_reports.filter(sector__icontains=sector)
                # print(reports[5])
            if not projects == "":
                reports[6] = all_reports.filter(projects__icontains=projects)
                # print(reports[6])
            if not time_created == "":
                reports[7] = all_reports.filter(time_created__icontains=time_created)
                # print(reports[7])

            checks[0] = form.cleaned_data['and_title']
            checks[1] = form.cleaned_data['and_company_name']
            checks[2] = form.cleaned_data['and_ceo']
            checks[3] = form.cleaned_data['and_location']
            checks[4] = form.cleaned_data['and_country']
            checks[5] = form.cleaned_data['and_sector']
            checks[6] = form.cleaned_data['and_projects']
            checks[7] = form.cleaned_data['and_time_created']

            final_reports = []

            for i in range(0,8):
                if checks[i] == False:
                    # print("doing union")
                    final_reports = union(final_reports, reports[i])
                    # print(final_reports)
                else:
                    # print("doing intersection")
                    final_reports = intersection(final_reports, reports[i])


            # print(len(final_reports))
            #
            # # TEST TODO remove
            for report in final_reports:
                print(report.title)

            return render(request, 'home.html',)
        else:
            return render(request, 'searches/advanced_search.html', {'form': AdvancedSearchForm()})
    else:
        return render(request, 'searches/advanced_search.html', {'form': AdvancedSearchForm()})

def union(lst1, lst2):
    return list(set(lst1).union(set(lst2)))

def intersection(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))
