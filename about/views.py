from django.shortcuts import render 
#from django.http import HttpResponse


def about(request): 
  return render(request, 'about.html')

def home(request):
    return render(request, 'about.html')

def privacy_policy(request): 
  return render(request, 'privacy_policy.html')

#def about(request):
 #   return render(request, 'about.html')


# def custom_404_view(request, exception):
  #  return render(request, '404.html', status=404)

