from enum import Enum


class RoomType(Enum):
    INDIVIDUAL_STUDY = 'I'
    GROUP_STUDY = 'G'


class Location(Enum):
    GROUND_FLOOR = 0
    MAIN_FLOOR = 1
    SECOND_FLOOR = 2


class Room(object):
    def __init__(self):
        self.id = None
        self.room_number = None
        self.capacity = None
        self.location = None
        self.room_type = None
