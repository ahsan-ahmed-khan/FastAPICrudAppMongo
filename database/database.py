import motor.motor_asyncio

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.MONGO_URI = "mongodb://localhost:27017"
        self.dbName = "nodes"
        self.collectionName = "nodes"

    async def connect(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.MONGO_URI)
        self.db = self.client[self.dbName]

    async def close(self):
        self.client.close()

    def get_collection(self):
        return self.db[self.collectionName]

database = Database()
