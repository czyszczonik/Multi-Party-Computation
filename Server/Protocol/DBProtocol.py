from .Client import getMongoClient
from .Protocol import Protocol
from .Result import Result
from .ResultRounds import ResultRound1


def getProtocolById(protocolID):
    client = getMongoClient()
    return Protocol(client.protocol.find_one({"protocolID" : protocolID}))


def getProtocolByName(name1, name2):
    client = getMongoClient()
    filter = { "$or": [ { "$and": [ {'iniciator': f"{user1}"},{'responder': f"{user2}"}]}, { "$and": [ {'iniciator': f"{user1}"},{'responder': f"{user2}"}]}]}
    return Protocol(client.protocol.find_one(filter)).getData()

def getOpenProtocols(name):
    client = getMongoClient()
    filter = { "$or": [ {'iniciator': f"{name}"},{'responder': f"{name}"}]}
    return client.protocol.find(filter)

def getActiveProtocols(name):
    proto = getOpenProtocols(name)
    results = []
    for data in proto:
        current = Protocol(data)
        if current.isTurn(name):
            results.append(current.getData().toDictionary())
    return results


def removeProtocol(protocolID):
    client = getMongoClient()
    filter = {"protocolID" : protocolID}
    client.protocol.delete_one(filter)

def removeSecrets(protocolID):
    client = getMongoClient()
    filter = {"protocolID" : protocolID}
    client.secret.delete_many(filter)


def protocolExistis(user1, user2):
    client = getMongoClient()
    filter = { "$or": [ { "$and": [ {'iniciator': f"{user1}"},{'responder': f"{user2}"}]}, { "$and": [ {'iniciator': f"{user1}"},{'responder': f"{user2}"}]}]}
    result = client.protocol.find_one(filter)
    return result != None


def putFirstRound(data):
    client = getMongoClient()
    proto = ResultRound1(data)
    client.protocol.insert_one(proto.toDictionary())


def putSecondRound(protocolID, v):
    client = getMongoClient()
    filter = { "protocolID": f"{protocolID}" }
    update = { "$set": { "v": f"{v}", "round": "2" } }
    client.protocol.update_one(filter, update)


def putThirdRound(protocolID, iniciatorChecks):
    client = getMongoClient()
    filter = { "protocolID": f"{protocolID}" }
    update = { "$set": { "iniciatorChecks": f"{iniciatorChecks}", "round": "3" } }
    client.protocol.update_one(filter, update)


def putFourthRound(protocolID, responderLabels):
    client = getMongoClient()
    filter = { "protocolID": f"{protocolID}" }
    update = { "$set": { "iniciatorChecks": f"{responderLabels}", "round": "4" } }
    client.protocol.update_one(filter, update)


def putResult(user1, user2, result):
    client = getMongoClient()
    result = Result(user1, user2, result)
    client.result.insert_one(result.toDictionary())
