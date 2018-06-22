from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("<h1> Hello World Homepage blank url (for now) </h1>")


# Create your views here.
