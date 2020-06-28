class Profile():
    def __init__(self, username, firstName = None, lastName = None):
        if username is None:
            return None
        dict = username
        self.username = dict.get('username', {})
        self.firstName = dict.get('firstName', {})
        self.lastName = dict.get('lastName', {})
        self.age = {}
        self.bio = {}
        self.imageUrl = {}
        self.phone = {}


    def toDictionary(self):
        return self.__dict__