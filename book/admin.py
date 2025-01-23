from django.contrib import admin
from .models import TimeSlot, Appointment, Booking

admin.site.register(TimeSlot)
admin.site.register(Appointment)

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

admin.site.register(Booking, BookingAdmin)
