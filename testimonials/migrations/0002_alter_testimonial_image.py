# Generated by Django 4.2.17 on 2025-01-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='assets/images/testimonials/'),
        ),
    ]
