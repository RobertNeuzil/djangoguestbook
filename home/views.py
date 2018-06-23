from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm


def index(request):
	xyz = MyForm()
	return render(request, 'home/index.html', {"xyz": xyz})


# Create your views here.
