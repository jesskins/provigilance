from django import forms
from .models import Testimonial
import datetime 

class TestimonialForm(forms.ModelForm):
    MONTH_CHOICES = [
        ('', 'Select a month'),
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    
    current_year = datetime.datetime.now().year
    YEAR_CHOICES = [(year, year) for year in range(2006, current_year + 1)]

    service_month = forms.ChoiceField(choices=MONTH_CHOICES, required=True)
    service_year = forms.ChoiceField(choices=YEAR_CHOICES, required=True)

    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'company', 'role', 'text', 'image', 'service_month', 'service_year']
        widgets = { 
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}), 
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}), 
            'company': forms.TextInput(attrs={'placeholder': 'Enter your company name, or the company you represent'}), 
            'role': forms.TextInput(attrs={'placeholder': 'Enter your job role'}), 
            'text': forms.Textarea(attrs={'placeholder': 'Write your testimonial here...'}), 
            'image': forms.ClearableFileInput(attrs={'placeholder': 'Optional: Upload an image'}), 
            'service_month': forms.Select(attrs={'placeholder': 'In which month did you access our service?'}), 
            'service_year': forms.Select(attrs={'placeholder': 'And, in which year?'}), 
            }
