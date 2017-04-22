import unittest
from LRRS.DBManager.DBHandler import dbHandler
from LRRS.Entities.User import User
from LRRS.Entities.Room import RoomType
from LRRS.Entities.Booking import BookingStatus, Booking
from datetime import datetime, timedelta

class TestDBHandler(unittest.TestCase):

    def test_validate_user(self):
        archit = User("archit")
        archit.set_password("123")
        assert dbHandler.validate_user(archit) is False

        archit.set_password("a123")
        assert dbHandler.validate_user(archit)

    def test_get_a_room(self):
        room = dbHandler.get_a_room("100A")
        assert room.room_number=="100A"

    def test_get_individual_rooms(self):
        rooms = dbHandler.get_individual_rooms()
        for room in rooms:
            assert room.room_type == RoomType.INDIVIDUAL_STUDY

    def test_group_rooms(self):
        rooms = dbHandler.get_group_rooms()
        for room in rooms:
            assert room.room_type == RoomType.GROUP_STUDY


    def test_get_bookings(self):
        date = datetime.today().date()
        bookings = dbHandler.get_bookings("110C", date)
        if bookings is not None:
            for booking in bookings:
                assert booking.booking_status in [BookingStatus.ACTIVE, BookingStatus.NOT_STARTED]


    def test_save_booking(self):
        booking = Booking()
        booking.booking_name = "Test Save"
        booking.start_date = datetime.today().date()
        booking.end_date = booking.start_date
        booking.start_time = (datetime.today() + timedelta(minutes=15)).time()
        booking.end_time = (datetime.today() + timedelta(minutes=75)).time()
        booking.room_number = "Test Room"
        booking.user= User("archit")
        booking_id = dbHandler.save_booking(booking)
        the_booking = dbHandler.get_booking(booking_id)
        assert booking_id == the_booking.booking_id

    def test_get_booking(self):
        booking_id = 1
        booking = dbHandler.get_booking(booking_id)
        if booking is not None:
            assert booking.booking_id == booking_id

    def test_update_booking_status(self):
        booking_id = 1
        booking = dbHandler.get_booking(booking_id)
        if booking.booking_status == BookingStatus.NOT_STARTED:
            dbHandler.update_booking_status(booking_id, BookingStatus.ACTIVE)
            booking = dbHandler.get_booking(booking_id)
            assert booking.booking_status == BookingStatus.ACTIVE
        elif booking.booking_status == BookingStatus.ACTIVE:
             dbHandler.update_booking_status(booking_id, BookingStatus.COMPLETED)
             booking = dbHandler.get_booking(booking_id)
             assert booking.booking_status == BookingStatus.COMPLETED


    def test_get_current_inactive_bookings(self):
        bookings = dbHandler.get_current_inactive_bookings()
        ct = datetime.now().time()
        current_time = datetime(year=1900, month=1, day=1, hour=ct.hour, minute=ct.minute, second=ct.second)
        test_time = current_time - timedelta(minutes=15)
        if bookings is not None:
            for booking in bookings:
                assert booking.booking_status == BookingStatus.NOT_STARTED
                assert booking.start_time >= test_time

