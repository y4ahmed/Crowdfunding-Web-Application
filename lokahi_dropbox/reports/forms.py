from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from groups.models import Group
from .models import Report, File, ReportPermissions


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'compName', 'ceo', 'phoneNum', 'location',
                  'sector', 'projects', 'private', 'email')
        exclude = ('AES_key', 'time_created', 'owner')


class ReportPermissionsForm(ModelForm):
    class Meta:
        model = ReportPermissions
        fields = ('allowed_users', 'allowed_groups')

    def __init__(self, *args, **kwargs):
        super(ReportPermissionsForm, self).__init__(*args, **kwargs)
        self.fields["allowed_users"].widget = CheckboxSelectMultiple()
        self.fields["allowed_users"].help_text = ""
        self.fields["allowed_users"].queryset = User.objects.all()
        self.fields["allowed_groups"].widget = CheckboxSelectMultiple()
        self.fields["allowed_groups"].help_text = ""
        self.fields["allowed_groups"].queryset = Group.objects.all()


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('title', 'is_encrypted', 'upload')
