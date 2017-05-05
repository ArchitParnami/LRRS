from interface import Interface
from LRRS.Entities.User import User

class IDBHandler(Interface):

    def validate_user(self, oUser:User):
        pass

    def get_user(self, username):
        pass

    def get_individual_rooms(self):
        pass

    def get_a_room(self, room_number):
        pass

    def get_group_rooms(self):
        pass

    # gets active or not started bookings
    def get_bookings(self, room_number, booking_date):
        pass

    def get_user_bookings(self, username):
        pass


    def save_booking(self, booking):
        pass

    def get_booking(self, booking_id):
        pass

    def update_booking_status(self, booking_id, new_status):
        pass

    def get_current_inactive_bookings(self):
        pass