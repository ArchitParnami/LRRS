from LRRS.DBManager.DBQueries import DBQueries as DBQ
from LRRS.Entities import Booking, Room, User
from LRRS.App import mysql

class DBHandler():


    def validate_user(self, oUser:User):
        query = DBQ.CHECK_USER_QUERY(oUser)
        print(query)
        return self.execute_boolean_query(query)


    def execute_boolean_query(self, query):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        count = cursor.fetchone()
        cursor.close()
        conn.close()
        return count[0] > 0

dbHandler = DBHandler()
