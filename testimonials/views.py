from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Testimonial
from .forms import TestimonialForm

# Create your views here.

def index(request):
    testimonials = Testimonial.objects.filter(approved=True)
    return render(request, 'testimonials/testimonials_list.html', {'testimonials': testimonials})

def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            send_mail( 'Thank you for your Testimonial Submission', 
            'Dear {},\n\nThank you for submitting your testimonial! We appreciate your feedback.\n\nKind Regards,\nMike Howkins, Provigilance'.format(form.cleaned_data['name']), 'provigilancetestimonial@gmail.com', 
            [form.cleaned_data['email']], 
            fail_silently=False, 
            ) 
            return redirect('submit_success')

    else:
        form = TestimonialForm()
    return render(request, 'testimonials/submit_testimonial.html', {'form': form})

def submit_success(request):
    return render(request, 'testimonials/submit_success.html')



# unsure if i will need these later, keeping in case

#def index(request):
 #   return render(request, 'testimonials/testimonials_list.html')

#def index(request):
 #   if request.method == "POST":
  #      return HttpResponse("You must have POSTed something")
   # else:
    #    return HttpResponse(request.method)

