from jproperties import Properties


class PropertiesHolder:
    _properties = Properties()
    _initialized = False

    _BOT_TOKEN = "discord.bot.token"
    _OWNER_AUTH_TOKEN = "discord.owner.token"

    @classmethod
    def get_bot_token(cls):
        return cls.get_property(cls._BOT_TOKEN)

    @classmethod
    def get_owner_token(cls):
        return cls.get_property(cls._OWNER_AUTH_TOKEN)

    @classmethod
    def get_property(cls, key):
        if not cls._initialized:
            cls._init()

        return cls._properties.get(key).data

    @classmethod
    def _init(cls):
        with open("application.properties", "rb") as properties_file:
            cls._properties.load(properties_file, encoding="utf-8")
