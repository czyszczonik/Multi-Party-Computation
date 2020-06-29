class Result():
    def __init__(self, user1, user2 = None, result = None):
        if user2 is not None:
            self.user1 = user1
            self.user2 = user2
            self.result = result
        else:
            self.user1 = user1.get("user1")
            self.user2 = user1.get("user2")
    def toDictionary(self):
        return self.__dict__
