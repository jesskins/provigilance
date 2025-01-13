from django.shortcuts import render
from django.http import HttpResponse

def my_about(request):
    return HttpResponse("Hello, this is the about/home page")