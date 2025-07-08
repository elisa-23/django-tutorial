from django.shortcuts import render
from django.http import HttpResponse

#name of function doesn't have to be the same as application
def questions(request): 
    return HttpResponse("Hello world!")

#HttpResponse = returns input onto the webpage