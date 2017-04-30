#from django.shortcuts import render
import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render, get_object_or_404

from messaging.models import Message
from .forms import ReportForm, FileForm, ReportPermissionsForm
from .models import Report, File, CompanyDetails


#Nothing working, not putting my stuff in yet
def can_view_report(user, report):
    return True if report.permissions.allowed_users.filter(pk=user.pk) or user.groups.filter(
        pk__in=[g.pk for g in report.permissions.allowed_groups.all()]) else False

FileFormset = inlineformset_factory(Report, File, form=FileForm, extra=0)
#Nothing working, not putting my stuff in yet

def createReport(request):
    #company_user = CompanyDetails.objects.get(user=request.user)
    company_user = request.user
    username = None
    if request.user.is_authenticated():
        username = request.user
    has_messages = False
    #some stuff about messages
    message_list = Message.objects.filter(receiver=request.user)
    for m in message_list:
        if m.opened == False:
            has_messages = True
            break
    if company_user or is_site_manager(request.user):
        if request.method == 'POST':
            report_form = ReportForm(request.POST, prefix="report_form")
            permissions_form = ReportPermissionsForm(request.POST, prefix="permissions_form")

            file_formset = FileFormset(request.POST, request.FILES, prefix="file_formset")

            if report_form.is_valid() and permissions_form.is_valid() and file_formset.is_valid():
                report = report_form.save(commit=False)
                report.owner = request.user
                #report.company_name = getattr(company_user,'company_name')
                #report.company_phone = getattr(company_user,'company_phone')
                #report.company_location = getattr(company_user,'company_location')
                #report.company_country = getattr(company_user,'company_country')
                report.has_attachments = False
                report.save()

                permissions = permissions_form.save(commit=False);
                permissions.report = report;
                permissions.save();
                permissions_form.save_m2m();

                for form in file_formset:
                    file = form.save(commit=False)
                    file.upload_date = datetime.date.today()
                    file.report = report
                    file.save()

                if File.objects.filter(report__pk=report.pk):
                    report.has_attachments = True;
                else:
                    report.has_attachments = False;

                report.save()

                messages.success(request, "Report created")
                return redirect('viewReport')
        else:
            report_form = ReportForm(prefix="report_form")
            permissions_form = ReportPermissionsForm(prefix="permissions_form")
            file_formset = FileFormset(prefix="file_formset")
        return render(request, 'reports/createReport.html',
                      {'report_form': report_form, 'permissions_form': permissions_form, 'file_formset': file_formset,
                       'has_messages': has_messages, 'username': username})

    else:
        return redirect('viewReport', {'has_messages': has_messages, 'username': username})


@login_required
def viewReport(request, pk):
    username = None
    if request.user.is_authenticated():
        username = request.user
    has_messages = False
    #message_list = Message.objects.filter(receiver=request.user)
    #for m in message_list:
    #    if m.opened == False:
    #        has_messages = True
    #        break
    report = get_object_or_404(Report, pk=pk)
    is_owner = (report.owner.pk == request.user.pk)

    if not report.private or is_owner or can_view_report(request.user, report):
        unencrypted_files = File.objects.filter(report__pk=report.pk, is_encrypted=False)
        has_encrypted_files = True if File.objects.filter(report__pk=report.pk, is_encrypted=True) else False
        # checks if user is in report group or is a collaborator
        return render(request, 'viewReport.html', {'report': report, 'is_owner': is_owner,
                                                           'unencrypted_files': unencrypted_files,
                                                           'has_encrypted_files': has_encrypted_files,
                                                           'has_messages': has_messages, 'username': username})
    else:
        return redirect('home', {'has_messages': has_messages, 'username': username})


@login_required
def editReport(request, pk):
    username = None
    if request.user.is_authenticated():
        username = request.user
    has_messages = False
    #message_list = Message.objects.filter(receiver=request.user)
    #for m in message_list:
    #    if m.opened == False:
    #        has_messages = True
    #        break
    report = get_object_or_404(Report, pk=pk)

    # Apparently only managers should be allowed to edit reports
    if not report.owner.pk == request.user.pk:
        return redirect('home')

    if request.method == 'POST':
        report_form = ReportForm(request.POST, instance=report)
        permissions_form = ReportPermissionsForm(request.POST, instance=report.permissions)
        file_formset = FileFormset(request.POST, request.FILES, instance=report)
        
        if report_form.is_valid() and permissions_form.is_valid() and file_formset.is_valid():
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

    return render(request, 'reports/editReport.html',
                  {'report_form': report_form, 'permissions_form': permissions_form, 'report': report,
                   'file_formset': file_formset, 'has_messages': has_messages, 'username': username})

