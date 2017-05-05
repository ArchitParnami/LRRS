from interface import implements
from LRRS.DBManager.DBQueries import DBQ
from LRRS.DBManager.DBConstants import DBC
from LRRS.Entities.Booking import Booking
from LRRS.Entities.Room import Room, Location, RoomType
from LRRS.Entities.User import User
from LRRS.DBManager.ORM import ORM
from LRRS.DBManager.IDBHandler import IDBHandler
from LRRS.App import mysql

class DBHandler(implements(IDBHandler)):

    def validate_user(self, oUser:User):
        query = DBQ.CHECK_USER(oUser)
        return self.__execute_boolean_query(query)

    def get_user(self, username):
        query = DBQ.GET_USER(username)
        data = self.__execute_data_query(query)
        users = ORM.UserMapper(data)
        if len(users) > 0:
            return users[0]
        else:
            return None

    def get_individual_rooms(self):
        data = self.__execute_data_query(DBQ.GET_INDIVIDUAL_ROOMS())
        return ORM.RoomMapper(data)

    def get_a_room(self, room_number):
        data = self.__execute_data_query(DBQ.GET_A_ROOM(room_number))
        room = ORM.RoomMapper(data)[0]
        return room

    def get_group_rooms(self):
        data = self.__execute_data_query(DBQ.GET_GROUP_ROOMS())
        return ORM.RoomMapper(data)

    # gets active or not started bookings
    def get_bookings(self, room_number, booking_date):
        booking_date = ORM.date_to_string(booking_date)
        query = DBQ.GET_ROOM_BOOKINGS(room_number, booking_date)
        data = self.__execute_data_query(query)
        return ORM.BookingMapper(data)

    def get_user_bookings(self, username):
        data = self.__execute_sp_read(DBC.SP_GET_USER_BOOKINGS, [username])
        return ORM.BookingMapper(data)


    def save_booking(self, booking):
        st = ORM.time_to_string(booking.start_time)
        et = ORM.time_to_string(booking.end_time)

        args = (booking.user.username, booking.start_date,
                booking.booking_name, booking.room_number, st, et, booking.end_date)

        data = self.__execute_sp_write(DBC.SP_BOOKING, args)
        booking_id = int(data[0][0])
        return booking_id

    def get_booking(self, booking_id):
        query = DBQ.GET_BOOKING(booking_id)
        data = self.__execute_data_query(query)
        booking = ORM.BookingMapper(data)[0]
        return booking

    def update_booking_status(self, booking_id, new_status):
        new_status = ORM.enum_to_booking_status[new_status]
        query = DBQ.UPDATE_BOOKING_STATUS(booking_id, new_status)
        self.__execute_query(query)

    def get_current_inactive_bookings(self):
        data = self.__execute_sp_read(DBC.SP_GET_CURRENT_INACTIVE_BOOKINGS, ())
        return ORM.BookingMapper(data)

    def __execute_boolean_query(self, query):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        count = cursor.fetchone()
        cursor.close()
        conn.close()
        return count[0] > 0

    def __execute_data_query(self, query):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        conn.close()
        return data

    def __execute_query(self, query):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    def __execute_sp_write(self, sp, args):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc(sp, args)
        conn.commit()
        conn.close()
        data = cursor.fetchall()
        return data

    def __execute_sp_read(self, sp, args):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc(sp, args)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data



dbHandler = DBHandler()
