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
