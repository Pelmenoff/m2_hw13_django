from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

def get_mongodb():
    password = os.environ.get('MONGO_KEY')
    client = MongoClient(password, server_api=ServerApi('1'))
    client.admin.command('ismaster')
    db = client.Mongodb
    return db