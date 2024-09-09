from fastapi import FastAPI
from router import route
from services.sites import SiteMongoClient
from pymongo.mongo_client import MongoClient

app = FastAPI()

client = SiteMongoClient("mongodb://127.0.0.1:27017/", "admin")

app.include_router(route.get_router(client))
