from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Testimonial
from .forms import TestimonialForm
import subprocess
import os


def index(request):
    testimonials = Testimonial.objects.filter(approved=True)
    return render(request, 'testimonials/testimonials_list.html',
                {'testimonials': testimonials})


def testimonials_list(request):
    return render(request, 'testimonials/testimonials_list.html')


def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and get the testimonial instance
            testimonial = form.save()
            print("Testimonial saved:", testimonial)

            recipient_email = testimonial.email
            recipient_name = testimonial.name
            print(f"Email: {recipient_email}, Name: {recipient_name}")

            # Call the send_email.py script with the recipient's email and name
            script_path = os.path.join(os.path.dirname(__file__), 'send_email.py')
            subprocess.call(['python', script_path, recipient_email, recipient_name])

            return redirect('submit_success')
    else:
        form = TestimonialForm()
    return render(request, 'testimonials/submit_testimonial.html', 
                    {'form': form})


def submit_success(request):
    return render(request, 'testimonials/submit_success.html')
