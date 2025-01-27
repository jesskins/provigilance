# book/utils.py
from datetime import timedelta, datetime, date
from .models import TimeSlot

def generate_timeslots():
    # Clear all existing timeslots
    TimeSlot.objects.all().delete()
    print("All timeslots deleted.")

    start_date = date(2025, 2, 1)  # Start from February 1st
    end_date = start_date + timedelta(days=365)  # Adjust as needed

    for single_date in (start_date + timedelta(n) for n in range((end_date - start_date).days)):
        if single_date.weekday() < 5:  # Monday to Friday
            for hour in range(8, 19):
                slot_type = 'AM' if hour < 12 else 'PM'
                duration = 'FD' if hour == 8 else 'HD'

                # Create new timeslots and log details
                timeslot, created = TimeSlot.objects.get_or_create(
                    day=single_date,
                    slot_type=slot_type,
                    defaults={'duration': duration, 'is_available': True}
                )

                if created:
                    print(f"Created timeslot for {single_date} at {hour}:00")
                else:
                    print(f"Timeslot for {single_date} at {hour}:00 already exists")

    print('Successfully generated timeslots')
