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
from book import views as book_views
from contact import views as contact_views
from django.conf import settings 
from django.conf.urls.static import static 
#from django.conf.urls import handler404

urlpatterns = [
    path('', about_views.home, name='home'),
    path('about/', about_views.home, name='about'),
    path('testimonials/', testimonials_views.index, name='testimonials'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('testimonials/submit/', testimonials_views.submit_testimonial, name='submit_testimonial'),
    path('testimonials/success/', testimonials_views.submit_success, name='submit_success'),
    path('contact/', contact_views.index, name='contact'),
    path('book/', book_views.index, name='book'),
    path('calendar/', book_views.calendar_view, name='calendar_view'),
    path('privacy-policy/', about_views.privacy_policy, name='privacy_policy'),
    path('admin/', admin.site.urls),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Custom 404 handler 

#handler404 = 'about.views.custom_404'
