from apscheduler.schedulers.background import BackgroundScheduler
from datetime import  datetime, timedelta

class BookingScheduler(object):
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.isRunning = False


    def schedule_booking(self, booking, func, args):
        triggerAt = datetime(year=booking.start_date.year,
                      month=booking.start_date.month,
                      day=booking.start_date.day,
                      hour=booking.start_time.hour,
                      minute=booking.start_time.minute,
                      second=booking.start_time.second)

        triggerAt = triggerAt + timedelta(minutes=15)
        self.scheduler.add_job(func, 'date', run_date=triggerAt, args=args,id=str(booking.booking_id))


    def start(self):
        if not self.isRunning:
            self.scheduler.start()
            self.isRunning = True



