from LRRS.DBManager.DBHandler import dbHandler
from LRRS.Entities.Room import RoomType
from LRRS.Entities.Booking import Booking, BookingStatus
from LRRS.Entities.User import User
from LRRS.Scheduler.BookingScheduler import BookingScheduler
from LRRS.Entities.MailService import MailService

from datetime import datetime
from datetime import timedelta


class BookingManager(object):
    def __init__(self):
        self.end_of_day_time = datetime.strptime('23:59:59', '%H:%M:%S')
        self.individual_rooms = dbHandler.get_individual_rooms()
        self.group_rooms = dbHandler.get_group_rooms()
        self.bookingScheduler = BookingScheduler()
        self.__schedule_inactive_bookings()
        self.mail_service = MailService()

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
                booking = self.__create_booking(username, room_number, start_date, start_time, end_time, booking_name)
                self.__schedule_booking(booking)
                return True
            else:
                # available at start but not for this duration
                return False
        else:
            # not availabile at start time
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
        booking_id = dbHandler.save_booking(booking)
        booking.booking_id = booking_id
        return booking

    def cancel_booking(self, booking_id):
        booking = dbHandler.get_booking(booking_id)
        if booking.booking_status in [BookingStatus.ACTIVE, BookingStatus.NOT_STARTED]:
            dbHandler.update_booking_status(booking_id, BookingStatus.CANCELLED)

    def get_booking(self, booking_id):
        return dbHandler.get_booking(booking_id)

    def __schedule_inactive_bookings(self):
        '''gets all bookings which are not started and whose start time > current time- 15 mins'''
        bookings = dbHandler.get_current_inactive_bookings()
        for booking in bookings:
            self.__schedule_booking(booking)
        self.bookingScheduler.start()

    def __schedule_booking(self, booking):
        self.bookingScheduler.schedule_booking(booking, self.__job_notify_cancel, [booking.booking_id])

    def __job_notify_cancel(self, booking_id):
        booking = self.get_booking(booking_id)
        if booking.booking_status == BookingStatus.NOT_STARTED:
            self.cancel_booking(booking.booking_id)
            message = "Hello " + booking.user + ",\n" + \
                      "Your booking for room " + booking.room_number + " from " + str(booking.start_time.time()) + " to " + \
                      str(booking.end_time.time()) + " on " + str(booking.start_date) + \
                      " has been cancelled because you did not check in."

            print(message)
            subj = "room reservation has been cancelled."
            toaddr = "username@uncc.edu"
            self.mail_service.send_mail(toaddr, subj, message)

booking_manager = BookingManager()
