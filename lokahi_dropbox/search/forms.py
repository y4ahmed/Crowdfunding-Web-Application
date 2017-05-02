import re
from django import forms
from reports.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, render

class BasicSearchForm(forms.Form):
    search = forms.CharField(max_length=1000)

class AdvancedSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)
    and_title = forms.BooleanField(required=False)
    company_name = forms.CharField(max_length=255, required=False)
    and_company_name = forms.BooleanField(required=False)
    ceo = forms.CharField(max_length=255, required=False)
    and_ceo = forms.BooleanField(required=False)
    location = forms.CharField(max_length=255, required=False)
    and_location = forms.BooleanField(required=False)
    country = forms.CharField(max_length=255, required=False)
    and_country = forms.BooleanField(required=False)
    sector = forms.CharField(max_length=255, required=False)
    and_sector = forms.BooleanField(required=False)
    projects = forms.CharField(required=False)
    and_projects = forms.BooleanField(required=False)
    time_created = forms.CharField(required=False)
    and_time_created = forms.BooleanField(required=False)
