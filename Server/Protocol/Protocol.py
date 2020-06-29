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
        return RoundData2(self.protocolID, self.encryptions, self.iniciatorChoice, self.pubKey, self.iniciatorMessages)

    def getRoundData3(self):
        return RoundData3(self.protocolID, self.v)

    def getRoundData4(self):
        return RoundData4(self.protocolID, self.iniciatorChecks)

    def computeResult(self):
        for key in self.iniciatorLabels:
            if self.iniciatorLabels[key] in self.responderLabels:
                res = int(key[1])
        return res

    def isTurn(self, name):
        if name == self.iniciator:
            return int(self.round) == 2
        elif name == self.responder:
            return int(self.round) == 1 or int(self.round) == 3

    def getData(self):
        if self.round == 1:
            return self.getRoundData2()
        elif self.round == 2:
            return self.getRoundData3()
        elif self.round == 4:
            return self.getRoundData3()
        else:
            return self
