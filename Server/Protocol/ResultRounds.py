import secrets, string
get_random_string = lambda size: ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(size))

class ResultRound1():
    def __init__(self, data):
        self.iniciator = data.get("iniciator", {})
        self.responder = data.get("responder", {})
        self.protocolID = get_random_string(64)
        self.round =  1
        self.encryptions = data.get("encryptions", {})
        self.iniciatorChoice = data.get("iniciatorChoice", {})
        self.iniciatorLabels = data.get("iniciatorLabels", {})
        self.pubKey = data.get("pubKey", {})
        self.iniciatorMessages = data.get("iniciatorMessages", {})

    def toDictionary(self):
        return self.__dict__
