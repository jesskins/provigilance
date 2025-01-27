from django import forms
from .models import Booking, TimeSlot

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'preferred_contact_type', 'preferred_contact_time', 'company', 'service_type', 'start_date', 'start_time', 'duration', 'returning_customer', 'message']
        widgets = {
            'start_date': forms.SelectDateWidget(),
        }

    def clean_start_date(self):
        start_date = self.cleaned_data['start_date']
        if not TimeSlot.objects.filter(day=start_date, is_available=True).exists():
            raise forms.ValidationError("No available timeslot for the selected date.")
        return start_date
