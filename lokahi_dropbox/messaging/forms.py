import re
from django import forms
from messaging.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, render
from django.contrib import messages

class MessageForm(forms.Form):

    subject = forms.CharField(max_length=30)
    message = forms.CharField(max_length=255)
    receiver = forms.CharField(max_length=255)
    encrypt = forms.BooleanField(required=False)

    def validate(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['receiver'])
        except User.DoesNotExist:
            raise forms.ValidationError(_('Invalid receiver name. Try again.'), code='invalid') #TODO: fix this to redirect to the same page


class DeleteForm(forms.Form):
    message = forms.CharField(max_length=30)
