from Secret import Secret
from Client import getMongoClient

def insertSecret(username, protocolId, secret):
    client = getMongoClient()
    data = Secret(username, protocolId, secret).toDictionary()
    client.secret.insert_one(data)

def getSecrets(username):
    client = getMongoClient()
    filter = {"username" : f"{username}"}
    secrets = client.secret.find(filter)
    list = []
    for element in secrets:
        list.append(Secret(element))
    return list

def removeSecret(username):
    client = getMongoClient()
    filter = {"username" : f"{username}"}
    client.secret.delete_one(filter)
