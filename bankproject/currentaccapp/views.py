from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def current_Account(request):
    return HttpResponse("<h1>Current Account - created Successfullly!</h1>")
