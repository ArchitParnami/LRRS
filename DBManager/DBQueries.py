from LRRS.DBManager.DBConstants import DBConstants as DBC
from LRRS.Entities.User import User

class DBQueries():

    def CHECK_USER_QUERY(oUser:User):

        query = "SELECT COUNT(*) FROM " + DBC.TABLE_USER +\
                " WHERE " + DBC.USER_USERNAME + " = '" + oUser.username + "' and " + \
                            DBC.USER_PASSWORD + " = '" + oUser.password + "';"

        return query