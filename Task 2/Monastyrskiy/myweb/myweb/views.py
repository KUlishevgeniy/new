from django.shortcuts import render
from django.http import Http404,HttpResponse


def index(request):
	print()
	render(request,"\static\index.html")



# Create your views here.
