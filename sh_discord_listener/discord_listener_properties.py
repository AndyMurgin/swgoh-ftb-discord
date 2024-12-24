from sh_properties.properties_discord_init import DiscordAppPropertiesHolder
from sh_properties.properties_init import init_properties
from sh_properties.properties_mongo_init import MongoPropertiesHolder


class DiscordListenerPropertiesHolder(
    DiscordAppPropertiesHolder, MongoPropertiesHolder
):
    __LOGGER_NAME_KEY = "discord.listener.log.logger.name"
    __LOG_FILE_KEY = "discord.listener.log.config.file"

    __DEFAULT_LISTEN_C3PO_TB = "discord.default.track_c3po_tb"
    __DEFAULT_LISTEN_C3PO_TW = "discord.default.track_c3po_tw"

    def __init__(self):
        super().__init__()

    def logger_name(self):
        return self._get_property(self.__LOGGER_NAME_KEY)

    def log_config_file(self):
        return self._get_property(self.__LOG_FILE_KEY)

    def get_default_track_c3po_tb(self):
        return self._get_property(self.__DEFAULT_LISTEN_C3PO_TB)

    def get_default_track_c3po_tw(self):
        return self._get_property(self.__DEFAULT_LISTEN_C3PO_TW)

    def _get_property(self, key):
        return DiscordAppPropertiesHolder.get_property_value(self, key)


def init_properties_for_discord_listener(
    properties_file: str,
) -> DiscordListenerPropertiesHolder:
    holder = DiscordListenerPropertiesHolder()
    init_properties(properties_file, holder)
    return holder
