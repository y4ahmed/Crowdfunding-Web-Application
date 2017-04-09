import re
from django import forms
from messaging.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class MessageForm(forms.Form):

    # message = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs={'required': True, 'max_length': 100, 'class':'select'}), label=_("message"))

    message = forms.CharField(max_length=255)
    receiver = forms.CharField(max_length=255)

    def validate(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['receiver'])
        except User.DoesNotExist:
            raise forms.ValidationError(_('Invalid receiver name. Try again.'), code='invalid') #TODO: fix this to redirect to the same page

    # def clean_username(self):
    #     try:
    #         user = User.objects.get(username__iexact=self.cleaned_data['username'])
    #     except User.DoesNotExist:
    #         return self.cleaned_data['username']
    #     raise forms.ValidationError(_("The username already exists. Please try another one."))
    #
    # def clean(self):
    #     if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
    #         if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #             raise forms.ValidationError(_("The two password fields did not match."))
    #     return self.cleaned_data
