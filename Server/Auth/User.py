from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, user_json):
        if user_json is None:
            self.username = None
            self.password = None
            self.firstName = None
            self.secondName = None
            self.salt = None
        else:
            self.username = user_json.get('username')
            self.password = user_json.get('password')
            self.firstName = user_json.get('firstName')
            self.lastName = user_json.get('lastName')
            self.salt = user_json.get('salt')

    def get_id(self):
        return self.username
        
    def toDictionary(self):
        return self.__dict__
