from django import forms

class First(forms.Form):
	First = forms.CharField(max_length=100, 
		widget= forms.TextInput(attrs={ "name": "firstname"} ))
class Last(forms.Form):
	Last = forms.CharField(max_length= 100,
		widget= forms.TextInput(attrs={"name": "lastname"} ))