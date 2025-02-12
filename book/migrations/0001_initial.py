# Generated by Django 4.2.17 on 2025-01-21 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('slot_type', models.CharField(choices=[('AM', 'Morning'), ('PM', 'Afternoon'), ('FD', 'Full Day')], max_length=2)),
                ('duration', models.CharField(choices=[('HD', 'Half Day'), ('FD', 'Full Day')], max_length=2)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.timeslot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

    
