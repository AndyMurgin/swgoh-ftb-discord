from pymongo import MongoClient

mongo = MongoClient("localhost", 27017)
db = mongo["seal_hunter_db"]