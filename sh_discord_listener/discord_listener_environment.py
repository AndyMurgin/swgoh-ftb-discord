from discord_listener_properties import DiscordListenerPropertiesHolder
from sh_environment.environment import Environment


class DiscordListenerEnv(Environment):
    def __init__(self, properties_holder: DiscordListenerPropertiesHolder):
        super().__init__(properties_holder)
