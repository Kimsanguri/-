import pymongo
import json
import pandas as pd


username = 'tkdgus5868'
password = '1234'
cluster_name = 'rentcluster.6shjq7e.mongodb.net'
db_name = 'rentdb'
collection_name = 'rentcollectv2'


client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster_name}/{db_name}?retryWrites=true&w=majority")
db = client[db_name]
collection = db[collection_name]


data = pd.read_csv('전세2023v3.csv')


json_data = json.loads(data.to_json(orient='records'))
collection.insert_many(json_data)

