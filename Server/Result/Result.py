class Result():
    def __init__(self, user1, user2, result):
        self.user1 = user1
        self.user2 = user2
        self.result = result

    def toDictionary(self):
        return self.__dict__
