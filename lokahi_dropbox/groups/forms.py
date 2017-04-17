import re
from django import forms
from groups.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, render

class GroupForm(forms.Form):

    # message = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs={'required': True, 'max_length': 100, 'class':'select'}), label=_("message"))
    group_name = forms.CharField(max_length=30)
    member_list = forms.CharField(max_length=1000)
    report_list = forms.CharField(max_length=1000)


    def validate_members(self):
        try:
            for member in member_list:
                m = User.objects.get(username__iexact=member)
        except User.DoesNotExist:
            raise forms.ValidationError(_('Invalid receiver name. Try again.'), code='invalid') #TODO: fix this to redirect to the same page

    # TODO once the report model is added
    def validate_reports(self):
        pass

    # TODO:
    # validate if the same group name already exists
    # validate if the members exist
    # validate if the reports are available
