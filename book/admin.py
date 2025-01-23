from django.contrib import admin
from .models import TimeSlot, Booking  # Removed Appointment

admin.site.register(TimeSlot)
admin.site.register(Booking)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('name', 'email')
    actions = ['approve_bookings', 'reject_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(status='A')
    approve_bookings.short_description = "Mark selected bookings as approved"

    def reject_bookings(self, request, queryset):
        queryset.update(status='R')
    reject_bookings.short_description = "Mark selected bookings as rejected"

