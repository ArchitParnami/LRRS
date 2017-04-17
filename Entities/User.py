class User(object):
    def __init__(self, username):
        self.username = username
        self.password = None

    def set_password(self, password):
        self.password = password
