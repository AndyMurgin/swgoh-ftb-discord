from pymongo import MongoClient

from .configs import PropertiesHolder

_mongo = MongoClient(
    PropertiesHolder.get_mongo_host(), PropertiesHolder.get_mongo_port()
)
db = _mongo[PropertiesHolder.get_mongo_db_name()]
