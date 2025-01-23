from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

def index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            timeslot = TimeSlot.objects.get(day=booking.date)
            timeslot.is_available = False
            timeslot.save()
            booking.timeslot = timeslot
            booking.save()
            return redirect('booking_success')
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