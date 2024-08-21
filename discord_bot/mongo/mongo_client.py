from pymongo import MongoClient

from discord_bot.configs import PropertiesHolder

mongo = MongoClient(
    PropertiesHolder.get_mongo_host(), PropertiesHolder.get_mongo_port()
)
db = mongo[PropertiesHolder.get_mongo_db_name()]
