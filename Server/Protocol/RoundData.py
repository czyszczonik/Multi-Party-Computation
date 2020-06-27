class RoundData2():
    def __init__(self, protocolID, encryptions, iniciatorChoice, pubKey, iniciatorMessages):
        self.protocolID = protocolID
        self.round = 2
        self.encryptions = encryptions
        self.iniciatorChoice = iniciatorChoice
        self.pubKey = pubKey
        self.iniciatorMessages = iniciatorMessages

    def toDictionary(self):
        return self.__dict__

class RoundData3():
    def __init__(self, protocolID, v):
        self.protocolID = protocolID
        self.round = 3
        self.v = v

    def toDictionary(self):
        return self.__dict__

class RoundData4():
    def __init__(self, protocolID, iniciatorChecks):
        self.protocolID = protocolID
        self.round = 4
        self.iniciatorChecks = iniciatorChecks

    def toDictionary(self):
        return self.__dict__
