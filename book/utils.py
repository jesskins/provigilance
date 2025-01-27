# book/utils.py
from datetime import timedelta, datetime
from book.models import TimeSlot

def generate_timeslots():
    # Ensure all existing timeslots are deleted
    TimeSlot.objects.all().delete()
    print("All timeslots deleted.")

    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=365)  # Adjust as needed

    for single_date in (start_date + timedelta(n) for n in range((end_date - start_date).days)):
        if single_date.weekday() < 5:  # Monday to Friday
            for hour in range(8, 19):
                slot_type = 'AM' if hour < 12 else 'PM'
                duration = 'FD' if hour == 8 else 'HD'

                # Create new timeslots
                TimeSlot.objects.create(
                    day=single_date,
                    slot_type=slot_type,
                    duration=duration,
                    is_available=True,
                )
                print(f'Created timeslot for {single_date} at {hour}:00')

    print('Successfully generated timeslots')
