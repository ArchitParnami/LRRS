from DBManager.DBQueries import DBQ
from DBManager.DBConstants import DBC
from Entities.Booking import Booking
from Entities.Room import Room, Location, RoomType
from Entities.User import User
from DBManager.ORM import ORM



from App import mysql

class DBHandler():

    def notify_booking(self,booking_id):
        query = DBQ.NOTIFY_BOOKING(booking_id)
        return self.__execute_update_query(query)

    def cancel_booking(self,booking_id):
        query = DBQ.CANCEL_BOOKING(booking_id)
        return self.__execute_update_query(query)


    def validate_user(self, oUser:User):
        query = DBQ.CHECK_USER(oUser)
        return self.__execute_boolean_query(query)

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

    def get_bookings(self, room_number, booking_date):
        query = DBQ.GET_ROOM_BOOKINGS(room_number, booking_date)
        data = self.__execute_data_query(query)
        return ORM.BookingMapper(data)

    def get_user_bookings(self, username):
        data = self.__execute_sp_read(DBC.SP_GET_USER_BOOKINGS, [username])
        return ORM.BookingMapper(data)

    def search_rooms(self, start_date, start_time, room_type):
        args = (room_type, start_time, start_date)
        return self.__execute_sp_read(DBC.SP_SEARCH_ROOMS, args)

    def save_booking(self, booking):

        st = ORM.time_to_string(booking.start_time)
        et = ORM.time_to_string(booking.end_time)

        args = (booking.user.username, booking.start_date,
                booking.booking_name, booking.room_number, st, et, booking.end_date)

        self.__execute_sp_write(DBC.SP_BOOKING, args)


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
        #cursor.close()
        conn.close()
        return data

    def __execute_update_query(self, query):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        # cursor.close()
        conn.close()
        return cursor.rowcount

    def __execute_sp_write(self, sp, args):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc(sp, args)
        conn.commit()
        cursor.close()
        conn.close()

    def __execute_sp_read(self, sp, args):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc(sp, args)
        data = cursor.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        return data


dbHandler = DBHandler()
