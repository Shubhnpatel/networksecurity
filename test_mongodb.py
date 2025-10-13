import os
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("URL")

client = MongoClient(url)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB")
except Exception as e:
    print(e)
