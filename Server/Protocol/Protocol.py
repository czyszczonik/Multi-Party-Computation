from .RoundData import RoundData2, RoundData3, RoundData4
class Protocol:
    def __init__(self, data):
        self.iniciator = data.get('iniciator', {})
        self.responder = data.get('responder', {})
        self.protocolID = data.get('protocolID', {})
        self.round = data.get('round', {})
        self.encryptions = data.get('encryptions', {})
        self.iniciatorChoice = data.get('iniciatorChoice', {})
        self.iniciatorLabels = data.get('iniciatorLabels', {})
        self.pubKey = data.get('pubKey', {})
        self.iniciatorMessages = data.get('iniciatorMessages', {})
        self.v = data.get('v', {})
        self.iniciatorChecks = data.get('iniciatorChecks', {})
        self.responderLabels = data.get('responderLabels', {})


    def getRoundData2(self):
        return RoundData2(self.protocolID, self.encryptions, self.iniciatorChoice, self.pubKey, self.iniciatorMessages).toDictionary()

    def getRoundData3(self):
        return RoundData3(self.protocolID, self.v).toDictionary()

    def getRoundData4(self):
        return RoundData4(self.protocolID, self.iniciatorChecks).toDictionary()

    def computeResult(self):
        for key in self.iniciatorLabels:
            if self.iniciatorLabels[key] in self.responderLabels:
                res = int(key[1])
        return res

    def isTurn(self, name):
        if name == self.iniciator:
            return self.round == 2
        elif name == self.responder:
            return self.round == 1 or self.round == 3

    def getData(self):
        if self.round == 1:
            return getRoundData2()
        elif self.round == 2:
            return getRoundData3()
        elif self.round == 4:
            return getRoundData3()
        else:
            return self
