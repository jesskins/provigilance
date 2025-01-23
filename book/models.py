from django.db import models
from django.contrib.auth.models import User

class TimeSlot(models.Model):
    SLOT_CHOICES = [
        ('AM', 'Morning'),
        ('PM', 'Afternoon'),
        ('FD', 'Full Day'),
    ]

    DURATION_CHOICES = [
        ('HD', 'Half Day'),
        ('FD', 'Full Day'),
    ]

    day = models.DateField(unique=True)
    slot_type = models.CharField(max_length=2, choices=SLOT_CHOICES)
    duration = models.CharField(max_length=2, choices=DURATION_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.day} - {self.get_slot_type_display()} ({self.get_duration_display()})"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
