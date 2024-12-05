from sh_properties.properties_discord_init import DiscordAppPropertiesHolder
from sh_properties.properties_init import init_properties


class DiscordListenerPropertiesHolder(DiscordAppPropertiesHolder):
    __LOGGER_NAME_KEY = "discord.listener.log.logger.name"
    __LOG_FILE_KEY = "discord.listener.log.config.file"

    def __init__(self):
        super().__init__()

    def logger_name(self):
        return self._get_property(self.__LOGGER_NAME_KEY)

    def log_config_file(self):
        return self._get_property(self.__LOG_FILE_KEY)

    def _get_property(self, key):
        return DiscordAppPropertiesHolder.get_property_value(self, key)


def init_properties_for_discord_listener(
    properties_file: str,
) -> DiscordListenerPropertiesHolder:
    holder = DiscordListenerPropertiesHolder()
    init_properties(properties_file, holder)
    return holder
