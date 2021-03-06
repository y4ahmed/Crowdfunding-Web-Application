from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from search.forms import BasicSearchForm, AdvancedSearchForm
from frontend.models import BaseUser
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
# from django.contrib.auth.models import User


# Create your views here.


@csrf_protect
def basic_search(request):
    if request.method == "POST":
        form = BasicSearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            base = BaseUser.objects.get(user=request.user)
            reports = base.reports.filter(title__icontains=search)
            # reports = reports.filter()
            # reports = Report.objects.filter(owner_id=request.user).filter(title__icontains=search)
            # TEST TODO remove
            # for report in reports:
            #     print(report.title)
            return render(
                request,
                'searches/search_result.html',
                {'report_list': reports, 'type': base.user_role}
            )
    base = BaseUser.objects.get(user=request.user)
    return render(
        request,
        'home.html',
        {
            'form': BasicSearchForm(),
            'user': base,
            'type': base.user_role,
            'invalid_search': True
        }
    )


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
            base_user = BaseUser.objects.get(user=request.user)
            all_reports = base_user.reports.all()

            if title == "" and company_name == "" and ceo == "" and \
                    location == "" and country == "" and sector == "" and \
                    projects == "" and time_created == "":
                return render(
                    request,
                    'searches/advanced_search.html',
                    {
                        'empty_field': True,
                        'type': base_user.user_role,
                        'form': AdvancedSearchForm()
                    }
                )

            if not title == "":
                reports[0] = all_reports.filter(title__icontains=title)
                # print(reports[0])
            if not company_name == "":
                reports[1] = all_reports.filter(
                    compName__icontains=company_name)
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
                try:
                    reports[7] = all_reports.filter(time_created=time_created)
                except (NameError, ValueError, ValidationError):
                    print("here")
                    return render(
                        request,
                        'searches/advanced_search.html',
                        {
                            'time_error': True,
                            'type': base_user.user_role,
                            'form': AdvancedSearchForm()
                        }
                    )

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

            for i in range(0, 8):
                if checks[i] is False:
                    # print("doing union")
                    final_reports = union(final_reports, reports[i])
                    # print(final_reports)
                else:
                    # print("doing intersection")
                    final_reports = intersection(final_reports, reports[i])

            # print(len(final_reports))
            # TODO comment out the next part!
            for report in final_reports:
                print(report.title)

            return HttpResponseRedirect('/home/')
        else:
            return render(
                request,
                'searches/advanced_search.html',
                {
                    'form': AdvancedSearchForm(),
                    'type': base_user.user_role,
                }
            )
    else:
        return render(
            request,
            'searches/advanced_search.html',
            {
                'form': AdvancedSearchForm(),
                'type': base_user.user_role,

            }
        )


def union(lst1, lst2):
    return list(set(lst1).union(set(lst2)))


def intersection(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))
