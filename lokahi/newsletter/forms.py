from django import forms

#creating our forms
class SignupForm(forms.Form):
	#django gives a number of predefined fields
	#CharField and EmailField are only two of them
	#go through the official docs for more field details
	name = forms.CharField(label='Enter your username', max_length=100)
	psswrd = forms.EmailField(label='Enter your password', max_length=100)