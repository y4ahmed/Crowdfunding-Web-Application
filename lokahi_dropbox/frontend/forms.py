import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class RegistrationForm(forms.Form):

    role_choices = (
        ("Company User", _("Company User")),
        ("Investor User", _("Investor User")),
    )
    # Keep common field attributes in a single place
    common_attrs = {'required': True,
                    'max_length': 30, 'class': 'form-control'}
    pass_attrs = {'required': True, 'max_length': 30,
                  'render_value': False, 'class': 'form-control'}
    # Form fields
    username = forms.RegexField(
        regex=r'^\w+$',
        widget=forms.TextInput(attrs=common_attrs),
        label=_("Username"),
        error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")
        }
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs=common_attrs),
        label=_("Email address")
    )
    pass1 = forms.CharField(
        widget=forms.PasswordInput(attrs=pass_attrs),
        label=_("Password")
    )
    pass2 = forms.CharField(
        widget=forms.PasswordInput(attrs=pass_attrs),
        label=_("Password (again)")
    )
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
        if 'pass1' in self.cleaned_data and 'pass2' in self.cleaned_data:
            if self.cleaned_data['pass1'] != self.cleaned_data['pass2']:
                raise forms.ValidationError(
                    _("The two password fields did not match."))
        return self.cleaned_data


class UploadFileForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'required': True, 'max_length': 30}),
        label=_("File Name")
    )
    file = forms.FileField(label=_("File"), allow_empty_file=True)
