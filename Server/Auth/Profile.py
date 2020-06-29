class Profile():
    def __init__(self, username, firstName = None, lastName = None):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.age = {}
        self.bio = {}
        self.imageUrl = {}
        self.phone = {}


    def toDictionary(self):
        return self.__dict__
