"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from about.views import home
from about import views as about_views
from testimonials import views as testimonials_views

urlpatterns = [
    path('', about_views.home, name='home'),
    path('about/', about_views.home, name='about'),
    path('testimonials/', testimonials_views.index, name='testimonials'),
    path('testimonials/submit/', testimonials_views.submit_testimonial, name='submit_testimonial'),
    path('testimonials/success/', testimonials_views.submit_success, name='submit_success'),
    path('admin/', admin.site.urls),
]
