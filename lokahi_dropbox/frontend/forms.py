import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):

    role_choices = (
        ("Company User", _("Company User")),
        ("Investor User", _("Investor User")),
    )

    username = forms.RegexField(regex=r'^\w+$',
                                widget=forms.TextInput(
                                    attrs={'required': True, 'max_length': 30, 'class': 'form-control'}),
                                label=_("Username"), error_messages={
                                    'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(attrs={'required': True, 'max_length': 30, 'class': 'form-control'}),
                             label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'required': True, 'max_length': 30, 'render_value': False, 'class': 'form-control'}), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'required': True, 'max_length': 30, 'render_value': False, 'class': 'form-control'}),
        label=_("Password (again)"))
    user_role = forms.ChoiceField(choices=role_choices)

    def clean_username(self):
        try:
            user = User.objects.get(
                username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            _("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    _("The two password fields did not match."))
        return self.cleaned_data


class UploadFileForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'required': True, 'max_length': 30}), label=_("File Name"))
    file = forms.FileField(label=_("File"), allow_empty_file=True)
