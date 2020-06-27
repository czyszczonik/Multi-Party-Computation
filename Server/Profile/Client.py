import pymongo

def getMongoClient():
    return pymongo.MongoClient("mongodb://localhost:27000/")['test']
