from sh_discord_listener import discord_listener_properties
from sh_discord_listener.discord_listener_environment import DiscordListenerEnv
from sh_ioc.service_locator import ServiceLocator
from sh_logging import log_init

locator = None

__LOGGER_COMPONENT_NAME = "logger"
__PROPERTIES_HOLDER_COMPONENT_NAME = "properties_holder"
__ENV_COMPONENT_NAME = "env"


class DiscordListenerServiceLocator(ServiceLocator):
    def __init__(self):
        super().__init__()

    def logger(self):
        global __LOGGER_COMPONENT_NAME
        return self.get_component(__LOGGER_COMPONENT_NAME)

    def properties_holder(self):
        global __PROPERTIES_HOLDER_COMPONENT_NAME
        return self.get_component(__PROPERTIES_HOLDER_COMPONENT_NAME)

    def env(self):
        global __ENV_COMPONENT_NAME
        return self.get_component(__ENV_COMPONENT_NAME)


def configure():
    global locator
    locator = DiscordListenerServiceLocator()

    properties_holder = (
        discord_listener_properties.init_properties_for_discord_listener(
            "application.properties"
        )
    )
    locator.load(__PROPERTIES_HOLDER_COMPONENT_NAME, properties_holder)

    locator.load(
        __LOGGER_COMPONENT_NAME,
        log_init.init_logger(
            properties_holder.logger_name(), properties_holder.log_config_file()
        ),
    )

    locator.load(__ENV_COMPONENT_NAME, DiscordListenerEnv(properties_holder))
