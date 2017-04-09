from enum import Enum


class BookingStatus(Enum):
    NOT_STARTED = 'NS'
    ACTIVE = 'AC'
    COMPLETED = 'CO'
    CANCELLED = 'CA'


class Booking(object):
    def __init__(self):
        self.user = None  # to be initialized with User object
        self.room_number = None  # room_number
        self.booking_id = None  # integer
        self.start_time = None  # datetime
        self.end_time = None  # datetime
        self.start_date = None  # datetime
        self.end_date = None  # datetime
        self.booking_name = None  # string
        self.booking_status = None  # BookingStatus Enum
