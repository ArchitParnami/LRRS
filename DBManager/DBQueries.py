from LRRS.DBManager.DBConstants import DBC
from LRRS.Entities.User import User
from LRRS.Entities.Room import RoomType
from LRRS.DBManager.ORM import ORM
from LRRS.Entities.Booking import BookingStatus


class DBQueries():
    def CHECK_USER(self, oUser: User):
        query = "SELECT COUNT(*) FROM " + DBC.TABLE_USER + \
                " WHERE " + DBC.USER_USERNAME + " = '" + oUser.username + "' and " + \
                DBC.USER_PASSWORD + " = '" + oUser.password + "';"
        return query

    def GET_INDIVIDUAL_ROOMS(self):
        query = "SELECT * FROM " + DBC.TABLE_ROOM + \
                " WHERE " + DBC.ROOM_TYPE + " = '" + ORM.enum_to_room_type[RoomType.INDIVIDUAL_STUDY] + "';"

        return query

    def GET_GROUP_ROOMS(self):
        query = "SELECT * FROM " + DBC.TABLE_ROOM + \
                " WHERE " + DBC.ROOM_TYPE + " = '" + ORM.enum_to_room_type[RoomType.GROUP_STUDY] + "';"

        return query

    def GET_ROOM_BOOKINGS(self, room_number, booking_date):
        query = "SELECT * FROM " + DBC.TABLE_BOOKING + \
                " WHERE " + DBC.BOOKING_ROOM_NUMBER + " ='" + room_number + "' and " + \
                DBC.BOOKING_START_DATE + " ='" + booking_date + "' and " + \
                DBC.BOOKING_STATUS + " in ('" + ORM.enum_to_booking_status[BookingStatus.ACTIVE] + "', '" + \
                                                ORM.enum_to_booking_status[BookingStatus.NOT_STARTED] + "');"

        return query

    def GET_A_ROOM(self, room_number):
        query = "SELECT * FROM " + DBC.TABLE_ROOM + " WHERE " + DBC.ROOM_NUMBER + " = '" + room_number + "';"
        return query

    def GET_BOOKING(self, booking_id):
        query = "SELECT *  FROM " + DBC.TABLE_BOOKING + " WHERE " + DBC.BOOKING_ID + " = '" + str(booking_id) + "';"
        return query

    def UPDATE_BOOKING_STATUS(self, booking_id, new_status):
        query = "UPDATE " + DBC.TABLE_BOOKING + \
                " SET " + DBC.BOOKING_STATUS + " = '" + new_status + "'" + \
                " WHERE " + DBC.BOOKING_ID + " = '" + str(booking_id) + "';"
        return query

    def GET_USER(self, username):
        query = "SELECT "+ DBC.USER_USERNAME + \
                " FROM " +  DBC.TABLE_USER + \
                " WHERE " + DBC.USER_USERNAME + " ='" + username + "';"
        return query

DBQ = DBQueries()
