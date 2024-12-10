from sh_discord_listener import discord_listener_properties
from sh_discord_listener.discord_listener_environment import DiscordListenerEnv
from sh_ioc.service_locator import ServiceLocator
from sh_logging import log_init

locator = None

_LOGGER_COMPONENT_NAME = "logger"
_PROPERTIES_HOLDER_COMPONENT_NAME = "properties_holder"
_ENV_COMPONENT_NAME = "env"


class DiscordListenerServiceLocator(ServiceLocator):
    def __init__(self):
        super().__init__()

    def logger(self):
        global _LOGGER_COMPONENT_NAME
        return self.get_component(_LOGGER_COMPONENT_NAME)

    def properties_holder(self):
        global _PROPERTIES_HOLDER_COMPONENT_NAME
        return self.get_component(_PROPERTIES_HOLDER_COMPONENT_NAME)

    def env(self):
        global _ENV_COMPONENT_NAME
        return self.get_component(_ENV_COMPONENT_NAME)


def configure(properties_file):
    global locator
    locator = DiscordListenerServiceLocator()

    properties_holder = (
        discord_listener_properties.init_properties_for_discord_listener(
            properties_file
        )
    )
    locator.load(
        _PROPERTIES_HOLDER_COMPONENT_NAME,
        properties_holder,
    )

    locator.load(
        _LOGGER_COMPONENT_NAME,
        log_init.init_logger(
            properties_holder.logger_name(), properties_holder.log_config_file()
        ),
    )

    locator.load(
        _ENV_COMPONENT_NAME,
        DiscordListenerEnv(properties_holder),
    )
