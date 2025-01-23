from django.shortcuts import render, redirect
from .models import TimeSlot, Booking
from .forms import BookingForm

def index(request):
    return render(request, 'book.html')

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

def booking_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')
