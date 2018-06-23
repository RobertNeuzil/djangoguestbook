from django import forms

class MyForm(forms.Form):
	textbox = forms.CharField(max_length=100)