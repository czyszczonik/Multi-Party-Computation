class ResultRound1():
    def __init__(self, iniciator, responder, encryptions, iniciatorChoice, iniciatorLabels, pubKey, iniciatorMessages):
        self.iniciator = iniciator
        self.responder = responder
        self.protocolID = get_random_string(64)
        self.round = 1
        self.encryptions = encryptions
        self.iniciatorChoice = iniciatorChoice
        self.iniciatorLabels = iniciatorLabels
        self.pubKey = pubKey
        self.iniciatorMessages = iniciatorMessages

    def toDictionary(self):
        return self.__dict__


class ResultRound2():
    def __init__(self, user, protocolID, v):
        self.user = user
        self.protocolID = protocolID
        self.v = v
        self.round = 2

    def toDictionary(self):
        return self.__dict__


class ResultRound3():
    def __init__(self, user, protocolID, iniciatorChecks):
        self.iniciatorChecks = iniciatorChecks
        self.user = user
        self.protocolID = protocolID
        self.round = 3

    def toDictionary(self):
        return self.__dict__

class ResultRound4():
    def __init__(self, user, protocolID, responderLabels):
        self.responderLabels = responderLabels
        self.user = user
        self.protocolID = protocolID
        self.round = 4

    def toDictionary(self):
        return self.__dict__
