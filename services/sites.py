from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Optional, List, Dict
from model.model import Site

class SiteMongoClient:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["sites"]
    
    def get(self, id: str) -> Site:
        document = self.collection.find_one({'_id': id})
        return Site.model_validate(document)
