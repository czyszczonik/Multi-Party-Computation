
class User():
    def __init__(self, username, password, salt):
        self.username = username
        self.password = password
        self.salt = salt


    def get_id(self):
        return self.username
        
    def toDictionary(self):
        return self.__dict__
