from django.shortcuts import render
from django.http import HttpResponse
from .forms import First, Last


def index(request):
	xyz = First()
	abc = Last()
	return render(request, 'home/index.html', {'xyz': xyz, 'abc': abc} )


# Create your views here.
