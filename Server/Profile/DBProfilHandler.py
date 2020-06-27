import pymongo
from Client import getMongoClient
from Profil import Profil

def createProfil(username, name, age, bio):
    client = getMongoClient()
    profil = Profil(username, name, age, bio).toDictionary()
    client.profil.insert_one(profil)

def getProfil(username):
    client = getMongoClient()
    return Profil(client.profil.find_one({"username" : f"{username}"}))

def updateUser(username, field, value):
    client = getMongoClient()
    filter = { "username": f"{username}" }
    update = { "$set": { f"{field}": f"{value}" } }
    client.profil.update_one(filter, update)

def removeProfil(username):
    client = getMongoClient()
    filter = { "username": f"{username}" }
    client.profil.delete_one(filter)
