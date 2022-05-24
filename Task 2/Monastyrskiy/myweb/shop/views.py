from django.shortcuts import render
from django.http import Http404,HttpResponse

def index(request):
	render(request,".\static\index.htm")



# Create your views here.
