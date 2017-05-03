import os
# from django.shortcuts import render
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.list import ListView
from messaging.models import Message
from .forms import ReportForm, FileForm, ReportPermissionsForm
from .models import Report, File, CompanyDetails
from frontend.models import BaseUser
from encryption import *


# Nothing working, not putting my stuff in yet
def can_view_report(user, report):
    can_view_report = False
    if report.permissions.allowed_users.filter(pk=user.pk) \
        or user.groups.filter(
            pk__in=[g.pk for g in report.permissions.allowed_groups.all()]
    ):
        return True
    return can_view_report


FileFormset = inlineformset_factory(Report, File, form=FileForm, extra=0)
# Nothing working, not putting my stuff in yet

def is_company_user(username):
    userRole = BaseUser.objects.get(user=username).user_role
    if userRole == "Company User":
        return True
    else:
        return False

def addReport(username,report):
    baseUser = BaseUser.objects.get(user=username)
    baseUser.reports.add(report)
    
def create_report(request):
    # company_user = CompanyDetails.objects.get(user=request.user)
    company_user = request.user
    username = None
    if request.user.is_authenticated():
        username = request.user
    has_messages = False
    # some stuff about messages
    message_list = Message.objects.filter(receiver=request.user)
    for m in message_list:
        if m.opened is False:
            has_messages = True
            break
    if company_user or is_site_manager(request.user):
        if request.method == 'POST':
            report_form = ReportForm(request.POST, prefix="report_form")
            permissions_form = ReportPermissionsForm(
                request.POST, prefix="permissions_form")

            file_formset = FileFormset(
                request.POST, request.FILES, prefix="file_formset")

            if report_form.is_valid() and permissions_form.is_valid() \
                    and file_formset.is_valid():
                report = report_form.save(commit=False)
                report.owner = company_user
                report.has_attachments = False
                report.save()

                permissions = permissions_form.save(commit=False)
                permissions.report = report
                permissions.save()
                permissions_form.save_m2m()

                for form in file_formset:
                    file = form.save(commit=False)
                    file.upload_date = datetime.date.today()
                    file.report = report
                    file.save()
                    if file.is_encrypted:
                        print(file.title)
                        encfile = encrypt_file("reportFiles/" + file.upload.__str__(), "encrypt")
                        a = os.path.dirname(
                            os.path.dirname(os.path.abspath(__file__))) + "/reportFiles/" + file.upload.__str__()
                        file.upload = encfile
                        os.remove(a)

                if File.objects.filter(report__pk=report.pk):
                    report.has_attachments = True
                else:
                    report.has_attachments = False

                report.save(force_update=True)
                addReport(request.user, report)
                messages.success(request, "Report created")
                return view_report(request, report.pk)
        else:
            report_form = ReportForm(prefix="report_form")
            permissions_form = ReportPermissionsForm(prefix="permissions_form")
            file_formset = FileFormset(prefix="file_formset")
        return render(
            request,
            'create_report.html',
            {
                'report_form': report_form,
                'permissions_form': permissions_form,
                'file_formset': file_formset,
                'username': username
            }
        )

    else:
        return redirect(
            'view_report',
            {'has_messages': has_messages, 'username': username}
        )


@login_required
def view_report(request, pk):
    username = None
    if request.user.is_authenticated():
        username = request.user
    has_messages = False
    # message_list = Message.objects.filter(receiver=request.user)
    # for m in message_list:
    #    if m.opened == False:
    #        has_messages = True
    #        break
    report = get_object_or_404(Report, pk=pk)
    is_owner = (report.owner.pk == request.user.pk)
    if not report.private or is_owner or can_view_report(request.user, report):
        unencrypted_files = File.objects.filter(
            report__pk=report.pk, is_encrypted=False)
        has_encrypted_files = True if File.objects.filter(
            report__pk=report.pk, is_encrypted=True) else False
        # checks if user is in report group or is a collaborator
        return render(
            request,
            'view_report.html',
            {
                'report': report, 'is_owner': is_owner,
                'unencrypted_files': unencrypted_files,
                'has_encrypted_files': has_encrypted_files,
                'has_messages': has_messages, 'username': username
            }
        )
    else:
        return redirect(
            'home',
            {'has_messages': has_messages, 'username': username}
        )


@login_required
def edit_report(request, pk):
    username = None
    if request.user.is_authenticated():
        username = request.user
    has_messages = False
    # message_list = Message.objects.filter(receiver=request.user)
    # for m in message_list:
    #    if m.opened == False:
    #        has_messages = True
    #        break
    report = get_object_or_404(Report, pk=pk)

    # Apparently only managers should be allowed to edit reports
    if not report.owner.pk == request.user.pk:
        return redirect('home')

    if request.method == 'POST':
        report_form = ReportForm(request.POST, instance=report)
        permissions_form = ReportPermissionsForm(
            request.POST, instance=report.permissions)
        file_formset = FileFormset(
            request.POST, request.FILES, instance=report)

        if report_form.is_valid() and permissions_form.is_valid() \
                and file_formset.is_valid():
            report_form.save()
            permissions_form.save()

            files = file_formset.save()

            for f in files:
                f.report = report
                if not f.upload_date:
                    f.upload_date = datetime.date.today()
                f.save()

            messages.success(request, "Report edited")
            return redirect('viewReport', pk=report.pk, )
    else:
        report_form = ReportForm(instance=report)
        permissions_form = ReportPermissionsForm(instance=report.permissions)
        file_formset = FileFormset(instance=report)

    return render(
        request,
        'reports/edit_report.html',
        {
            'report_form': report_form, 'permissions_form': permissions_form,
            'report': report, 'file_formset': file_formset,
            'has_messages': has_messages, 'username': username
        }
    )


@login_required
def delete_report(request, pk):
    report = get_object_or_404(Report, pk=pk)

    if is_site_manager(request.user) or report.owner.pk == request.user.pk:
        report.delete()

    return redirect('index')

class list_report(ListView):
    model = Report
    template_name = 'list_report.html'
    context_object_name = 'report_list'

    def get_queryset(self):
        username = self.request.user
        if is_site_manager(username):
            return Report.objects.all()
        else:
            return BaseUser.objects.get(user=username).reports.all()

def is_site_manager(username):
    userRole = BaseUser.objects.get(user=username).user_role
    if userRole =="Site Manager":
        return True
    else:
        return False
