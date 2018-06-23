from django import forms

class Email(forms.Form):
	EnterEmail = forms.EmailField(max_length=100)
class Web(forms.Form):
	EnterWeb = forms.URLField(max_length= 100)