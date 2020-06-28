from .Secret import Secret
from .Client import getMongoClient

def insertSecret(username, protocolId, secret):
    client = getMongoClient()
    data = Secret(username, protocolId, secret).toDictionary()
    client.secret.insert_one(data)

def fetchSecrets(username):
    client = getMongoClient()
    filter = {"username" : f"{username}"}
    secrets = client.secret.find(filter)
    # results = {}
    # for element in secrets:
    #     results[element['protocolId']] = Secret(element).toDictionary()
    results = []
    for element in secrets:
        results.append(Secret(element).toDictionary())
    return results

def fetchSecret(username, protocolId):
    client = getMongoClient()
    sec = client.secret.find_one({ "$and" : [{"username" : f"{username}"}, {"protocolId" : f"{protocolId}"}]})
    if sec is not None:
        return Secret(sec)
    else:
        return None

def removeSecret(username):
    client = getMongoClient()
    filter = {"username" : f"{username}"}
    client.secret.delete_one(filter)

