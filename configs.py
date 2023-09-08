from jproperties import Properties


class PropertiesHolder:
    __properties = Properties()
    __initialized = False

    __BOT_TOKEN = "discord.bot.token"
    __OWNER_AUTH_TOKEN = "discord.owner.token"
    __DEFAULT_NO_TAG_MODE = "discord.default.no_tag_mode"
    __DEFAULT_TRACK_TB = "discord.default.track_c3po_tb"

    @classmethod
    def get_bot_token(cls):
        return cls.get_property(cls.__BOT_TOKEN)

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
    def get_property(cls, key):
        if not cls.__initialized:
            cls._init()

        return cls.__properties.get(key).data

    @classmethod
    def _init(cls):
        with open("application.properties", "rb") as properties_file:
            cls.__properties.load(properties_file, encoding="utf-8")
