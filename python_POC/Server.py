class Server:
    def __init__(self):
        self.name = {}
        self.encryptions = {}
        self.ac = {}
        self.aliceLabels = {}
        self.pubKey = {}
        self.aliceMessages = {}
        self.v = {}
        self.bobMessages = {}
        self.bobLabels = {}
        self.secret = {}


    def computeResult(self):
        for key in self.aliceLabels:
            if self.aliceLabels[key] in self.bobLabels:
                res = int(key[1])
        return res

    def putRound1(self, encryptions, ac, aliceLabels, pubKey, aliceMessages):
        self.encryptions = encryptions
        self.ac = ac
        self.aliceLabels = aliceLabels
        self.pubKey = pubKey
        self.aliceMessages = aliceMessages

    def getRound2(self):
        return self.encryptions, self.ac, self.pubKey, self.aliceMessages

    def putRound2(self, v):
        self.v = v

    def getRound3(self):
        return self.v

    def putRound3(self, bobMessages):
        self.bobMessages = bobMessages

    def getRound4(self):
        return self.bobMessages

    def putRound4(self, bobLabels):
        self.bobLabels = bobLabels

    def storeSecret(self, name, secret):
        self.secret[name] = secret

    def getSecret(self, name):
        return self.secret[name]
