class Profil():
    def __init__(self, username, name = None, age = None, bio = None):
        if username is None:
            return None
        if age is None:
            dict = username
            self.username = dict.get('username')
            self.name = dict.get('name')
            self.age = dict.get('age')
            self.bio = dict.get('bio')
        else:
            self.username = username
            self.name = name
            self.age = age
            self.bio = bio

    def toDictionary(self):
        return self.__dict__

    def __str__(self):
        return f"Profil: Username:[{self.username}], name:[{self.name}], age:[{self.age}], bio:[{self.bio}],"
