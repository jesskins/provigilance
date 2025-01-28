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

    day = models.DateField()
    slot_type = models.CharField(max_length=2, choices=SLOT_CHOICES)
    duration = models.CharField(max_length=2, choices=DURATION_CHOICES)
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ('day', 'slot_type')

    def __str__(self):
        return f"{self.day} - {self.get_slot_type_display()} \
            ({self.get_duration_display()})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, default="Unknown")
    preferred_contact_type = models.CharField(max_length=50, default="Email")
    preferred_contact_time = models.CharField(
        max_length=50, blank=True, null=True, default="Anytime")
    company = models.CharField(max_length=100, default="Unknown Company")
    service_type = models.CharField(max_length=100, default="General")
    start_date = models.DateField()
    start_time = models.CharField(max_length=10, default="00:00")
    duration = models.IntegerField(default=1)  # Instead of length
    returning_customer = models.BooleanField(default=False)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='P')
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.name} - {self.start_date} at {self.start_time}"
