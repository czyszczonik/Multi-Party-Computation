import pymongo
from .Client import getMongoClient
from .Profile import Profile

def createProfile(username, name, age, bio):
    client = getMongoClient()
    profile = Profile(username, name, age, bio).toDictionary()
    client.profile.insert_one(profile)

def getProfileInfo(username):
    client = getMongoClient()
    return Profile(client.profile.find_one({"username" : f"{username}"}))

def updateProfileInfo(username, field, value):
    client = getMongoClient()
    filter = { "username": f"{username}" }
    update = { "$set": { f"{field}": f"{value}" } }
    client.profile.update_one(filter, update)

def removeProfile(username):
    client = getMongoClient()
    filter = { "username": f"{username}" }
    client.profile.delete_one(filter)
