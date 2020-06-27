from Result import Result
from Client import getMongoClient

def findResults(user1, user2):
    client = getMongoClient()
    return client.result.find_one({ "$or" : [{ "$and": [ {"user1" : f"{user1}"}, {"user2" : f"{user2}"}]}, { "$and": [ {"user1" : f"{user2}"}, {"user2" : f"{user1}"}]}]})

def putResult(user1, user2, result):
    client = getMongoClient()
    data = Result(user1, user2, result).toDictionary()
    client.result.insert_one(data)

def getResultForUser(user):
    client = getMongoClient()
    return client.result.find({ "$and" : [{ "$or": [ {'user1': f"{user}"},{'user2': f"{user}"}]}, {"result" : 1}]})
