from django import forms
from .models import Booking, TimeSlot


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name', 'email', 'phone_number', 'preferred_contact_type',
            'preferred_contact_time', 'company',
            'service_type', 'start_date', 'start_time', 'duration',
            'returning_customer', 'message']
        widgets = {
            'start_date': forms.SelectDateWidget(),
        }
