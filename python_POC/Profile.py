from random import randint

class Profile():
    def __init__(self, username, firstName = None, lastName = None):
        if firstName is not None:
            self.username = username
            self.firstName = firstName
            self.lastName = lastName
            self.age = randint(22, 30)
            self.bio = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sit amet lacus dolor. Duis velit turpis, lacinia ut congue in, cursus id odio. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Maecenas luctus efficitur ex eget gravida. Suspendisse id nisi porta, semper magna nec, porttitor quam."
            self.imageUrl = {}
            self.phone = f"{randint(101, 999)}-{randint(101, 999)}-{randint(101, 999)}"
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
