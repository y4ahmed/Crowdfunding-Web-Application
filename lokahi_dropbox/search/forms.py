import re
from django import forms
from reports.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, render

class BasicSearchForm(forms.Form):
    search = forms.CharField(max_length=1000)
