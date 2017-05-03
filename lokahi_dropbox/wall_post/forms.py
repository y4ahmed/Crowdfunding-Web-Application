import re
from django import forms
from wall_post.models import *
from messaging.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, render
from django.contrib import messages


class PostForm(forms.Form):
    message = forms.CharField(max_length=255)
    anonymous = forms.BooleanField(required=False)
