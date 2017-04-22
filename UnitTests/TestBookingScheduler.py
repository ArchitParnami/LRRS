import unittest
from LRRS.Scheduler.BookingScheduler import BookingScheduler
from LRRS.Entities.Booking import Booking, BookingStatus
from datetime import datetime, timedelta

class TestBookingScheduler(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBookingScheduler, self).__init__(*args, **kwargs)
        self.scheduler = BookingScheduler()
        self.scheduler.start()

    def job_test(self, booking_id):
        print("Test Booking: ", booking_id, "executed")

    def test_scheduler_booking(self):
        booking = Booking()
        booking.booking_id = 999
        booking.start_date = datetime.today()
        booking.start_time = (datetime.today() + timedelta(minutes=5))
        self.scheduler.schedule_booking(booking, self.job_test, [booking.booking_id])
        job = self.scheduler.get_job(booking.booking_id)
        assert job.id == str(booking.booking_id)


    def test_unschedule_booking(self):
        booking = Booking()
        booking.booking_id = 1000
        booking.start_date = datetime.today()
        booking.start_time = (datetime.today() + timedelta(minutes=5))
        self.scheduler.schedule_booking(booking, self.job_test, [booking.booking_id])
        self.scheduler.unschedule_booking(1000)
        job = self.scheduler.get_job(1000)
        assert job == None

