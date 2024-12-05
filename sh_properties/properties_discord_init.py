from .properties_init import PropertiesHolder, init_properties


class DiscordAppPropertiesHolder(PropertiesHolder):
    __DISCORD_BOT_TOKEN = "discord.bot.token"

    def __init__(self):
        super().__init__()

    def get_discord_bot_token(self):
        return PropertiesHolder.get_property_value(self, self.__DISCORD_BOT_TOKEN)


def init_properties_for_discord_app(properties_file: str) -> DiscordAppPropertiesHolder:
    holder = DiscordAppPropertiesHolder()
    init_properties(properties_file, holder)
    return holder
