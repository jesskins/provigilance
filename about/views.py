from django.shortcuts import render 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the about/home page")

def custom_404(request, exception):
    return render(request, '404.html', status=404)
