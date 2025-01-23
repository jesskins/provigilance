from django.contrib import admin
from django.urls import path
from about import views as about_views
from testimonials import views as testimonials_views
from book import views as book_views
from contact import views as contact_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', about_views.home, name='home'),
    path('about/', about_views.home, name='about'),
    path('testimonials/', testimonials_views.index, name='testimonials'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('testimonials/submit/', testimonials_views.submit_testimonial, name='submit_testimonial'),
    path('testimonials/success/', testimonials_views.submit_success, name='submit_success'),
    path('testimonials', testimonials_views.testimonials_list, name='testmonials_list'),
    path('contact/', contact_views.index, name='contact'),
    path('book/', book_views.booking_page, name='booking_page'),  # This should point to booking_page view
    path('booking_success/', book_views.booking_success, name='booking_success'),
    path('privacy-policy/', about_views.privacy_policy, name='privacy_policy'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
