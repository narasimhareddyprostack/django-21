from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def user_Account(request):
    return HttpResponse("<h1>User Account - created Successfullly!</h1>")
