from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'service_month', \
    'service_year', 'recommend', 'created_at')
    list_filter = ('service_year', 'recommend')
    search_fields = ('name', 'company', 'email', 'text')
