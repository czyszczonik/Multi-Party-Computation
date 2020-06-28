import pymongo
from .User import User
from .Client import getMongoClient

client = getMongoClient()

def createUser(user, profil):
    client.users.insert_one(user.toDictionary())
    client.profile.insert_one(profil.toDictionary())

def getUser(username):
    return User(client.users.find_one({"username" : f"{username}"}))

def getSalt(username):
    user = getUser(username)
    if user is None or user.salt is None:
        return None
    return user.salt

def getPasswordAndSalt(username):
    return getUser(username).password,  getUser(username).salt

def updateUser(username, field, value):
    filter = { "username": f"{username}" }
    update = { "$set": { f"{field}": f"{value}" } }
    client.users.update_one(filter, update)

def removeUser(username):
    filter = { "username": f"{username}" }
    client.users.delete_one(filter)