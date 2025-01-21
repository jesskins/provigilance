from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeSlot

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
