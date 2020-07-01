class RoundData2():
    def __init__(self, protocolID, encryptions, iniciatorChoice, pubKey, iniciatorMessages):
        self.protocolID = protocolID
        self.round = 2
        self.encryptions = encryptions
        self.iniciatorChoice = iniciatorChoice
        self.pubKey = pubKey
        self.iniciatorMessages = iniciatorMessages
        self.status = "true"

    def toDictionary(self):
        return self.__dict__

class RoundData3():
    def __init__(self, responder ,protocolID, v):
        self.protocolID = protocolID
        self.responder = responder
        self.round = 3
        self.v = v
        self.status = "true"

    def toDictionary(self):
        return self.__dict__

class RoundData4():
    def __init__(self, iniciator, protocolID, messagesForResponder):
        self.iniciator = iniciator
        self.protocolID = protocolID
        self.round = 4
        self.messagesForResponder = messagesForResponder
        self.status = "true"

    def toDictionary(self):
        return self.__dict__
