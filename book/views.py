from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm

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
