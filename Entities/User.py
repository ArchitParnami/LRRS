class User(object):
    def __init__(self, username):
        self.username = username
        self.password = None
        self.authentic = False

    def set_password(self, password):
        self.password = password

    def authenticate(self):
        self.authentic = True

    def is_authenticated(self):
        return self.authentic

    def is_active(self):
        return self.authentic

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username