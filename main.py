from pymongo import MongoClient
mongouri='mongodb+srv://pavani:p12345@cluster0.h1625.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client=MongoClient(mongouri)
db=client["Sacet"]
collection=db["cse"]
data={}
data["username"]="pavani"
data["password"]="p12345"
print("Username & Password")
print(data)


collection.insert_one(data) 
print("Data Inserted")
for i in collection.find({"username":"pavani"}):
    print(i)

   
collection.update_one(
     {"username":"pavani"},
      {"$set":{"password":"p12345"}}
    )
print(i)

collection.delete_one({"username":"pavani"})
print("Data deleted")
for i in collection.find():
    print(i)

