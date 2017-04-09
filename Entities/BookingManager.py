from LRRS.DBManager.DBHandler import dbHandler
from LRRS.Entities.Room import RoomType
from LRRS.Entities.Booking import Booking, BookingStatus
from LRRS.Entities.User import User

from datetime import datetime
from datetime import timedelta


class BookingManager(object):
    def __init__(self):
        self.end_of_day_time = datetime.strptime('23:59:59', '%H:%M:%S')
        self.individual_rooms = dbHandler.get_individual_rooms()
        self.group_rooms = dbHandler.get_group_rooms()

    def get_user_bookings(self, username):
        return dbHandler.get_user_bookings(username)

    def search(self, start_date, start_time, room_type):
        rooms = self.individual_rooms if room_type == RoomType.INDIVIDUAL_STUDY else self.group_rooms
        avail = []
        for room in rooms:
            room_bookings = dbHandler.get_bookings(room.room_number, start_date)
            availability = self.compute_room_availability(room, room_bookings, start_time)
            if availability is not None:
                avail.append(availability)

        return avail

    def compute_room_availability(self, room, bookings, start_time):

        if len(bookings) == 0:
            return (room, start_time, self.end_of_day_time)

        future_bookings = False
        booked = False

        diff_min = timedelta.max

        for booking in bookings:
            if booking.end_time > start_time:
                future_bookings = True
                if booking.start_time > start_time:
                    diff = booking.start_time - start_time
                    if diff < diff_min:
                        diff_min = diff
                else:
                    booked = True
                    break

        if not future_bookings:
            return (room, start_time, self.end_of_day_time)
        elif booked:
            return None
        else:
            return (room, start_time, start_time + diff_min)

    def try_book_room(self, room_number, start_date, start_time, end_time, username, booking_name):
        rooms = self.individual_rooms + self.group_rooms
        target_room = None
        for room in rooms:
            if room.room_number == room_number:
                target_room = room
                break

        if target_room is None:
            raise Exception("Room not found", room_number)

        current_bookings = dbHandler.get_bookings(target_room.room_number, start_date)
        availability = self.compute_room_availability(target_room, current_bookings, start_time)

        if availability is not None:
            _, avail_start, avail_end = availability
            if end_time <= avail_end:
                self.__create_booking(username, room_number, start_date, start_time, end_time, booking_name)
                return True
            else:
                #available at start but not for this duration
                return False
        else:
            #not availabile at start time
            return False

    def __create_booking(self, username, room_number, start_date, start_time, end_time, booking_name):
        booking = Booking()
        booking.user = User(username)
        booking.room_number = room_number
        booking.start_time = start_time
        booking.start_date = start_date
        booking.end_time = end_time
        booking.end_date = start_date
        booking.booking_name = booking_name
        booking.booking_status = BookingStatus.NOT_STARTED
        dbHandler.save_booking(booking)


booking_manager = BookingManager()


