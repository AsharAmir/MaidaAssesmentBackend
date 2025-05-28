import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
# Asynciomotorclient gives a client to connect to the database
client: AsyncIOMotorClient = AsyncIOMotorClient(MONGO_URI)
# Get the database
db = client["moderationdb"]
# Get the collections
tokens_collection = db["tokens"]
usages_collection = db["usages"]
