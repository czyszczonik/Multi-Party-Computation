from .RoundData import RoundData2, RoundData3, RoundData4
import json 

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
        self.messagesForResponder = data.get('messagesForResponder', {})
        self.responderLabels = data.get('responderLabels', {})
        self.status = "true"


    def getRoundData2(self):
        return RoundData2(self.protocolID, self.encryptions, self.iniciatorChoice, self.pubKey, self.iniciatorMessages)

    def getRoundData3(self):
        return RoundData3(self.responder, self.protocolID, self.v)

    def getRoundData4(self):
        return RoundData4(self.iniciator, self.protocolID, self.messagesForResponder)

    def computeResult(self):
        self.iniciatorLabels = json.loads(self.iniciatorLabels)
        try:
            for key in self.iniciatorLabels.keys():
                if self.iniciatorLabels[key] == self.responderLabels:
                    res = int(key[1])
        except Exception as e:
            print(e)
        return res

    def isTurn(self, name):
        if name == self.iniciator:
            return int(self.round) == 2
        elif name == self.responder:
            return int(self.round) == 1 or int(self.round) == 3

    def getData(self):
        if int(self.round)== 1:
            return self.getRoundData2()
        elif int(self.round) == 2:
            return self.getRoundData3()
        elif int(self.round) == 3:
            return self.getRoundData4()
        else:
            return self
