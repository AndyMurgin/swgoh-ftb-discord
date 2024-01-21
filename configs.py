from jproperties import Properties


class PropertiesHolder:
    __properties = Properties()
    __initialized = False

    __DISCORD_BOT_TOKEN = "discord.bot.token"
    __OWNER_AUTH_TOKEN = "discord.owner.token"
    __DEFAULT_NO_TAG_MODE = "discord.default.no_tag_mode"
    __DEFAULT_TRACK_TB = "discord.default.track_c3po_tb"

    __TELEGRAM_BOT_TOKEN = "telegram.bot.token"

    __MONGO_INIT = "mongo.init"
    __MONGO_HOST = "mongo.server.host"
    __MONGO_PORT = "mongo.server.port"
    __MONGO_DB_NAME = "mondo.db"

    @classmethod
    def get_discord_bot_token(cls):
        return cls.get_property(cls.__DISCORD_BOT_TOKEN)

    @classmethod
    def get_telegram_bot_token(cls):
        return cls.get_property(cls.__TELEGRAM_BOT_TOKEN)

    @classmethod
    def get_owner_token(cls):
        return cls.get_property(cls.__OWNER_AUTH_TOKEN)

    @classmethod
    def get_default_notag_mode(cls) -> bool:
        notag_value = cls.get_property(cls.__DEFAULT_NO_TAG_MODE)
        return bool(notag_value) if notag_value is not None else True

    @classmethod
    def get_default_track_c3po_tb(cls) -> bool:
        track_tb_value = cls.get_property(cls.__DEFAULT_TRACK_TB)
        return bool(track_tb_value) if track_tb_value is not None else None

    @classmethod
    def get_mongo_host(cls) -> str:
        mongo_host_value = cls.get_property(cls.__MONGO_HOST)
        return str(mongo_host_value) if mongo_host_value is not None else None

    @classmethod
    def get_mongo_port(cls) -> int:
        mongo_port_value = cls.get_property(cls.__MONGO_PORT)
        return int(mongo_port_value) if mongo_port_value is not None else None

    @classmethod
    def get_mongo_db_name(cls) -> str:
        mongo_db_value = cls.get_property(cls.__MONGO_DB_NAME)
        return str(mongo_db_value) if mongo_db_value is not None else None

    @classmethod
    def get_mongo_init(cls) -> str:
        return cls.get_property(cls.__MONGO_INIT)

    @classmethod
    def get_property(cls, key):
        if not cls.__initialized:
            cls._init()

        return cls.__properties.get(key).data

    @classmethod
    def _init(cls):
        with open("application.properties", "rb") as properties_file:
            cls.__properties.load(properties_file, encoding="utf-8")
