from LRRS.DBManager.DBConstants import DBC
from LRRS.Entities.User import User
from LRRS.Entities.Room import RoomType
from LRRS.DBManager.ORM import ORM

class DBQueries():

    def CHECK_USER(self, oUser:User):

        query = "SELECT COUNT(*) FROM " + DBC.TABLE_USER +\
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

        return  query

    def GET_ROOM_BOOKINGS(self, room_number, booking_date):

        query = "SELECT * FROM " + DBC.TABLE_BOOKING + \
                " WHERE " + DBC.BOOKING_ROOM_NUMBER + " ='" + room_number + "' and " + \
                DBC.BOOKING_START_DATE + " ='" + booking_date + "';"

        return query

    def GET_A_ROOM(self, room_number):
       query = "SELECT * FROM " + DBC.TABLE_ROOM + " WHERE " + DBC.ROOM_NUMBER + " = '" + room_number + "';"
       return query


DBQ = DBQueries()