from enum import Enum


class RoomType(Enum):
    INDIVIDUAL_STUDY = 'Individual Study'
    GROUP_STUDY = 'Group Study'


class Location(Enum):
    GROUND_FLOOR = 'Ground Floor'
    MAIN_FLOOR = 'Main Floor'
    SECOND_FLOOR = 'Second Floor'


class Room(object):
    def __init__(self):
        self.id = None
        self.room_number = None
        self.capacity = None
        self.location = None
        self.room_type = None
