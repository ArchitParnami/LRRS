from interface import implements
from LRRS.DBManager.DBQueries import DBQ
from LRRS.DBManager.DBConstants import DBC
from LRRS.Entities.Booking import Booking, BookingStatus
from LRRS.Entities.Room import Room, Location, RoomType
from LRRS.Entities.User import User
from LRRS.DBManager.ORM import ORM
from LRRS.DBManager.IDBHandler import IDBHandler
from datetime import datetime, timedelta

from LRRS.App import mysql


class MockDBHandler(implements(IDBHandler)):

    def __init__(self):
        self.users = {'aparnami' : '1234',
                      'dshah27': '1234',
                      'jma27': '1234'}

        self.rooms = [
            # ID, room_no, capacity, location, room_type
            ['1', 'GS-1', '2', 'G', 'I'], ['2', 'GS-2', '3', 'G', 'I'], ['3', 'GS-3', '2', 'G', 'I'],
            ['4', '100A', '2', 'M', 'I'], ['5', '100B', '3', 'M', 'I'], ['6', '100C', '2', 'M', 'I'],
            ['7', '110A', '4', 'M', 'G'], ['8', '110B', '5', 'M', 'G'], ['9', '110C', '7', 'M', 'G'],
            ['10','200A', '2', 'S', 'I'], ['11', '200B', '3', 'S', 'I'], ['12', '200C', '2', 'S', 'I'],
            ['13', '210A', '5', 'S', 'G'], ['14', '210B', '6','S', 'G'], ['15', '210C', '8', 'S', 'G']
        ]

        self.bookings = [

            # booking_id, uname, start_time, end_time, start_date, end_date, booking_status, booking_name, room_no

        ]

    def validate_user(self, oUser:User):
        if oUser.username in self.users:
            if self.users[oUser.username] == oUser.password:
                return True
        return False

    def get_user(self, username):
        data = []
        if username in self.users:
            data.append([username])
        users = ORM.UserMapper(data)
        if len(users) > 0:
            return users[0]
        else:
            return None

    def get_individual_rooms(self):
        data = [room for room in self.rooms if room[4] == 'I']
        return ORM.RoomMapper(data)

    def get_a_room(self, room_number):
        data = [room for room in self.rooms if room[1] == room_number]
        room = ORM.RoomMapper(data)[0]
        return room

    def get_group_rooms(self):
        data = [room for room in self.rooms if room[4] == 'G']
        return ORM.RoomMapper(data)


    def get_user_bookings(self, username):
        data = [booking for booking in self.bookings if booking[1] == username]
        return ORM.BookingMapper(data)

    def get_booking(self, booking_id):
        data = [booking for booking in self.bookings if booking[0] == booking_id]
        booking = ORM.BookingMapper(data)[0]
        return booking

    def update_booking_status(self, booking_id, new_status):
        new_status = ORM.enum_to_booking_status[new_status]
        for booking in self.bookings:
            if booking[0] == booking_id:
                booking[6] = new_status
                break

    def get_current_inactive_bookings(self):
        bookings = ORM.BookingMapper(self.bookings)
        result = []
        for booking in bookings:
            if booking.booking_status == BookingStatus.NOT_STARTED:
                b_date = ORM.string_to_date(booking.start_date).date()
                if b_date >= datetime.today().date():
                    b_time = booking.start_time.time()
                    time_now_15 = (datetime.today() - timedelta(minutes=15)).time()
                    if b_time >= time_now_15:
                        result.append(booking)

        return result

        # gets active or not started bookings
    def get_bookings(self, room_number, booking_date):
        booking_date = booking_date.date()
        data = [booking for booking in self.bookings if booking[8] == room_number and
                                                        booking[4] == booking_date and
                                                        booking[6] in ['NS', 'AC']]
        return ORM.BookingMapper(data)

    def save_booking(self, booking):

        id = str(len(self.bookings))
        st = timedelta(hours=booking.start_time.hour, minutes=booking.start_time.minute, seconds=booking.start_time.second)
        et = timedelta(hours=booking.end_time.hour, minutes=booking.end_time.minute,
                       seconds=booking.end_time.second)

        sd = booking.start_date.date()
        ed = booking.end_date.date()

        booking = [id, booking.user.username, st, et, sd, ed,
                   'NS', booking.booking_name, booking.room_number]

        self.bookings.append(booking)

        return id

dbHandler = MockDBHandler()
