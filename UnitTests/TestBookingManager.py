import unittest
from LRRS.Entities.BookingManager import booking_manager
from datetime import datetime, timedelta
from LRRS.Entities.Room import RoomType
from LRRS.DBManager.ORM import ORM
from LRRS.Entities.Booking import BookingStatus
import time

class TestBookingManager(unittest.TestCase):

    def test_search(self):
        start_date = datetime.today()
        start_time = (start_date + timedelta(minutes=30)) .time()
        start_time = ORM.time_to_string(start_time)
        start_time = ORM.string_to_time(start_time)
        results = booking_manager.search(start_date, start_time, RoomType.INDIVIDUAL_STUDY)

        if results is not None:
            print("Rooms are available")
        else:
            print("Rooms unavailable")

    def book_room(self, name):
        start_date = datetime.today()
        start_time = (start_date + timedelta(minutes=15)).time()
        start_time = ORM.time_to_string(start_time)
        start_time = ORM.string_to_time(start_time)

        avail = booking_manager.search(start_date, start_time, RoomType.GROUP_STUDY)

        end_time = start_time + timedelta(minutes=60)

        if avail is not None:
            room, startsAt, endsAt = avail[0]
            if end_time <= endsAt:
                book_till = end_time
            else:
                book_till = endsAt

            result, booking_id = booking_manager.try_book_room(room.room_number, start_date, startsAt, book_till, "aparnami", name)
            assert result == True
            return booking_id

    def test_book_room(self):
        self.book_room("test book")

    def test_check_in(self):
        booking_id = self.book_room("test check-in")
        time.sleep(2)
        booking_manager.check_in(booking_id)
        booking = booking_manager.get_booking(booking_id)
        assert booking.booking_status == BookingStatus.ACTIVE

    def test_cancel_booking(self):
        booking_id = self.book_room("test cancelled")
        time.sleep(2)
        booking_manager.cancel_booking(booking_id)
        booking = booking_manager.get_booking(booking_id)
        assert booking.booking_status == BookingStatus.CANCELLED

    def test_complete_booking(self):
        booking_id = self.book_room("test completed")
        time.sleep(2)
        booking_manager.check_in(booking_id)
        time.sleep(2)
        booking_manager.end_booking(booking_id)
        booking = booking_manager.get_booking(booking_id)
        assert booking.booking_status == BookingStatus.COMPLETED


if __name__ == '__main__':
    unittest.main()