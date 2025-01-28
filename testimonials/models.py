from django.db import models


class Testimonial(models.Model):
    RECOMMEND_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    image = models.ImageField(
        upload_to='testimonials/images', blank=True, null=True)
    approved = models.BooleanField(default=False)
    service_month = models.CharField(max_length=20, blank=True, null=True)
    recommend = models.CharField(max_length=3, choices=RECOMMEND_CHOICES)
    service_year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
