from Entities.Room import Room, Location, RoomType
from Entities.Booking import Booking
from datetime import datetime

class ObjectRelationalMapper(object):

    def __init__(self):
        self.time_format = "%H:%M:%S"
        self.location_to_enum = {"G": Location.GROUND_FLOOR,
                          "M": Location.MAIN_FLOOR,
                          "S": Location.SECOND_FLOOR}

        self.room_type_to_enum = {"I": RoomType.INDIVIDUAL_STUDY,
                           "G": RoomType.GROUP_STUDY}

        self.enum_to_location = {Location.GROUND_FLOOR: "G",
                                 Location.MAIN_FLOOR: "M",
                                 Location.SECOND_FLOOR: "S"}

        self.enum_to_room_type = {RoomType.INDIVIDUAL_STUDY: "I",
                                  RoomType.GROUP_STUDY: "G"}


    def RoomMapper(self, data):
        rooms = []
        for row in data:
            room = Room()
            room.id = row[0]
            room.room_number = row[1]
            room.capacity = row[2]
            room.location = self.location_to_enum[row[3]]
            room.room_type = self.room_type_to_enum[row[4]]
            rooms.append(room)
        return rooms

    def BookingMapper(self, data):
        bookings = []
        for row in data:
            booking = Booking()
            booking.booking_id = row[0]
            booking.user = row[1]
            booking.start_time = self.time_delta_to_time(row[2])
            booking.end_time = self.time_delta_to_time(row[3])
            booking.start_date = row[4]
            booking.end_date = row[5]
            booking.booking_status = row[6]
            booking.booking_name = row[7]
            booking.room_number = row[8]
            bookings.append(booking)
        return bookings

    def string_to_time(self, t):
        return datetime.strptime(t, self.time_format)

    def time_to_string(self, t):
        return t.strftime(self.time_format)

    def time_delta_to_time(self, delta):
        return datetime(1900, 1, 1) + delta


ORM = ObjectRelationalMapper()
