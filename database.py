from motor.motor_asyncio import AsyncIOMotorClient


class Db(object):
    
    def __init__(self, db_url, bot):
        self.bot = bot
        self.database = AsyncIOMotorClient(db_url).bot
