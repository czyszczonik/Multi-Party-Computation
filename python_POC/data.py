import pymongo
from Profile import Profile
from User import User

client = pymongo.MongoClient("mongodb://localhost:27000/")['test']
password = "8ad771c6c2f1465ffa434061b8b26c1214d306c2af70fce3d82134a3d83c08cbb521f20acfe704521dd33dffe4d488242adeb4d9e90d98f9a13d2bc4747c35a5"
salt = "FrAHzxXBZZJwyUMde1pd1j7oguVHx3mQ6cjSkYEQe/JDiJFeul2rU325hheM5B3v5JxGE9ykQThHxgY3LV3PbjEJ9HBSitTMgZTObg7Q+Vy2xzJn/6mhYkQS3p4YPY/qg1MGOaxzH4jJl9iQ3dxCQ4/DnBzkspBfOXtqI0BM0aQ="
firstname = "Gorska"
lastname = "Romana"
username = ["Roman", "Asia", "Filip"]
###################################################################################
#                                   CREATING                                      #
###################################################################################
# CREATE ROMANS
# for x in range(3):
#     un = username[x]
#     client.users.insert_one(User(un, password, salt).toDictionary())
#     client.profile.insert_one(Profile(un, un, lastname).toDictionary())





###################################################################################
#                                   DELETING                                      #
###################################################################################
# DELETE ROMANS
# for x in range(3):
    # client.users.delete_one({"username" : f"{username[x]}"})
# client.profile.delete_one({"username" : f"{username[x]}"})

client.users.drop()
client.profile.drop()
client.protocol.drop()
client.result.drop()
client.secret.drop()

# client.protocol.delete_one({"iniciator" : f"tom"})

# client.result.delete_one({"result" : 1})

# client.protocol.delete_one({"protocolId" : f"NGHWOZ6903N5LRNM72MNT5P0WC1EQ64BA41H6J2FTXE6FKL8AVG2OF2SEM0RH7JY"})

###################################################################################
#                                   UPDATING                                      #
###################################################################################
# filter = { "username": "admin1" }
# update = { "$set": { "responderLabels": "{}", "round": "3" } }
# client.profile.update_one(filter, update)

# filter = { "username": "admin1" }
# update = { "$set": { "firstName": "Filip", "lastName": "Górski", "bio" : "I like crypto!" } }
# client.profile.update_one(filter, update)
# res = client.profile.find_one(filter)
# print(res)

###################################################################################
#                                   FINDING                                       #
###################################################################################
print("_"*100)

for x in client.users.find():
    print(x)
print("_"*100)

for x in client.profile.find():
    print(x)
print("_"*100)


print("_"*100)
for x in client.result.find():
    print(x)
print("_"*100)


print("_"*100)
for x in client.protocol.find():
    print(x)
print("_"*100)

    
