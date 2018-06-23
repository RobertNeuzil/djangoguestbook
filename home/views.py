from django.shortcuts import render
from django.http import HttpResponse
from .forms import Email, Web


def index(request):
	xyz = Email()
	abc = Web()
	return render(request, 'home/index.html', {'xyz': xyz, 'abc': abc} )


# Create your views here.
