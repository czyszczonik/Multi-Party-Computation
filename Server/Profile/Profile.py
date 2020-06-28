class Profile():
    def __init__(self, username, firstName = None, lastName = None, age = None, bio = None, imageUrl = None, phone = None):
        if username is None:
            return None
        if firstName is None:
            dict = username
            self.username = dict.get('username', {})
            self.firstName = dict.get('firstName', {})
            self.lastName = dict.get('lastName', {})
            self.age = dict.get('age', {})
            self.bio = dict.get('bio', {})
            self.imageUrl = dict.get('imageUrl', {})
            self.phone = dict.get('phone', {})
        else:
            self.username = username
            self.firstName = firstName
            self.lastName = lastName     
            self.age = age
            self.bio = bio
            self.imageUrl = imageUrl
            self.phone = phone

    def toDictionary(self):
        return self.__dict__