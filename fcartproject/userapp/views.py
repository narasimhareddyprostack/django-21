from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(x):
	return HttpResponse('<h2>Login successfull!</h2>')
	
	
def logout(x):
	return HttpResponse('<h2>Logout successfull!</h2>')