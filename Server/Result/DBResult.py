from .Result import Result
from .Client import getMongoClient
from .Protocol import Protocol
from .Profile import Profile


def getPairs(user):
    client = getMongoClient()
    resultUsers = client.result.find({ "$and" : [{ "$or": [ {'user1': f"{user}"},{'user2': f"{user}"}]}, {"result" : 1}]})
    openProtocols = client.protocol.find({ "$or": [ {'iniciator': f"{user}"},{ "$and": [ {"round": {"$nin": [1]}},{'responder': f"{user}"}]}]})
    names = getNames(user, resultUsers, openProtocols)
    names.append(user)
    profiles = client.profile.find()
    result = []
    for profile in profiles:
        prof = Profile(profile)
        prof.phone = ''
        if prof.username not in names:
            result.append(prof.toDictionary())
    return result


def getResultsForUser(user):
    client = getMongoClient()
    resultUsers = client.result.find({ "$and" : [{ "$or": [ {'user1': f"{user}"},{'user2': f"{user}"}]}, {"result" : 1}]})
    names = getNames(user, resultUsers)
    results = []
    for name in names:
        prof = client.profile.find_one({"username" : name})
        results.append(Profile(prof).toDictionary())
    return results


def putResult(user1, user2, result):
    client = getMongoClient()
    data = Result(user1, user2, result).toDictionary()
    client.result.insert_one(data)


def findResults(user1, user2):
    client = getMongoClient()
    return client.result.find_one({ "$or" : [{ "$and": [ {"user1" : f"{user1}"}, {"user2" : f"{user2}"}]}, { "$and": [ {"user1" : f"{user2}"}, {"user2" : f"{user1}"}]}]})


def getNames(user, resultUsers, protocolUsers = []):
    names = []
    for element in resultUsers:
        entity = Result(element)
        if entity.user1 == user:
            names.append(entity.user2)
        else:
            names.append(entity.user1)
    for element in protocolUsers:
        entity = Protocol(element)
        if entity.iniciator == user:
            names.append(entity.responder)
        else:
            names.append(entity.iniciator)
    return names
