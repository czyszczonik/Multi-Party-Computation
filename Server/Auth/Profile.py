class Profile():
    def __init__(self, username, firstName = None, lastName = None):
        if firstName is not None:
            self.username = username
            self.firstName = firstName
            self.lastName = lastName
            self.age = ""
            self.bio = ""
            self.imageUrl = ""
            self.phone = ""
        else:
            self.username = username.get("username",{})
            self.firstName = username.get("firstName",{})
            self.lastName = username.get("lastName",{})
            self.age = username.get("age",{})
            self.bio = username.get("bio",{})
            self.imageUrl = username.get("imageUrl",{})
            self.phone = {}
    def toDictionary(self):
        return self.__dict__
