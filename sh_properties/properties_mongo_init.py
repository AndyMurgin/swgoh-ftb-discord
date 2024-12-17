from sh_properties.properties_init import PropertiesHolder, init_properties


class MongoPropertiesHolder(PropertiesHolder):
    __MONGO_HOST = "mongo.server.host"
    __MONGO_PORT = "mongo.server.port"
    __MONGO_DB_NAME = "mongo.db"

    def __init__(self):
        super().__init__()

    def get_mongo_host(self):
        return PropertiesHolder.get_property_value(self, self.__MONGO_HOST)

    def get_mongo_port(self):
        return PropertiesHolder.get_property_value(self, self.__MONGO_PORT)

    def get_mongo_db_name(self):
        return PropertiesHolder.get_property_value(self, self.__MONGO_DB_NAME)


def init_properties_for_discord_app(properties_file: str) -> MongoPropertiesHolder:
    holder = MongoPropertiesHolder()
    init_properties(properties_file, holder)
    return holder
