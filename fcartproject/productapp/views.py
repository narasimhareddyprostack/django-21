from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dispaly(request):
	return HttpResponse('<h1>Products are displaying</h1>')