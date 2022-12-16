import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:computer12@cluster0.kysmmcb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "yunish",
    "emailid" : "wyunish@gmail.com",
    "surname" : "khan"
}
db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)