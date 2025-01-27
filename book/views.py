# views.py
from django.shortcuts import render, redirect
from .models import Booking, TimeSlot  # Ensure TimeSlot is imported
from .forms import BookingForm

def index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            try:
                timeslot = TimeSlot.objects.filter(day=booking.start_date, is_available=True).first()  # Check for available timeslot
                if timeslot:
                    timeslot.is_available = False
                    timeslot.save()
                    booking.timeslot = timeslot
                    booking.save()
                    return redirect('booking_success')
                else:
                    form.add_error('start_date', 'No available timeslot for the selected date.')
            except TimeSlot.DoesNotExist:
                form.add_error('start_date', 'No available timeslot for the selected date.')
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

def calendar_view(request):
    timeslots = TimeSlot.objects.all()
    events = []

    for slot in timeslots:
        color = 'green' if slot.is_available else 'red'
        events.append({
            'title': slot.get_slot_type_display(),
            'start': slot.day.isoformat(),
            'color': color
        })

    return render(request, 'book.html', {'events': events})
