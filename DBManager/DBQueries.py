class DBQuery():
    def getUser(self, username):
        return "select * from user_info where username=username"