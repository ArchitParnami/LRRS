from enum import Enum


class BookingStatus(Enum):
    NOT_STARTED = 'NS'
    ACTIVE = 'AC'
    COMPLETED = 'CO'
    CANCELLED = 'CA'


class Booking(object):
    def __init__(self):
        self.user = None  # to be initialized with User object
        self.room = None  # to be initialized with Room object
        self.booking_id = None  # integer
        self.start_time = None  # string
        self.end_time = None  # string
        self.start_date = None  # string
        self.end_date = None  # string
        self.booking_name = None  # string
        self.booking_status = None  # BookingStatus Enum
