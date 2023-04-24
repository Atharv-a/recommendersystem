
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pickle
import pandas as pd

uri = "mongodb+srv://Atharva:0987A@cluster.cpafhoe.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

dis=pickle.load(open('/home/atharva/c++project/recommender_sys/dis.pkl','rb'))

db=client.list_database_names()
print(db)
db=client['Movie-recommender']
collection=db['distance']

for i in range(4806):
     collection.insert_one({
          "_id":i,
          "dis":list(dis[i])
     })



