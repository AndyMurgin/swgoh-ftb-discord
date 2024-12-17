from pymongo import MongoClient
from pymongo.database import Database

from sh_properties.properties_mongo_init import MongoPropertiesHolder


class MongoDatabase:
    def __init__(self, db: Database):
        self._db = db

    def db(self):
        return self._db

    def __getitem__(self, item):
        return self._db[item]


def mongo_init(properties: MongoPropertiesHolder) -> MongoDatabase:
    client = MongoClient(properties.get_mongo_host(), properties.get_mongo_port())
    return MongoDatabase(client[properties.get_mongo_db_name()])
