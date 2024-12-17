from c3po_validator import C3POValidator
from sh_discord_listener import discord_listener_properties
from sh_discord_listener.discord_listener_environment import DiscordListenerEnvironment
from sh_ioc.service_locator import ServiceLocator
from sh_logging import log_init
from sh_mongo import database_client

locator = None

_LOGGER_COMPONENT_NAME = "logger"
_PROPERTIES_HOLDER_COMPONENT_NAME = "properties_holder"
_ENV_COMPONENT_NAME = "env"
_C3PO_VALIDATOR_COMPONENT_NAME = "c3po_validator"
_MONGO_DATABASE_COMPONENT_NAME = "mongo_db"


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

    def c3po_validator(self):
        global _C3PO_VALIDATOR_COMPONENT_NAME
        return self.get_component(_C3PO_VALIDATOR_COMPONENT_NAME)

    def mongo_db(self):
        global _MONGO_DATABASE_COMPONENT_NAME
        return self.get_component(_MONGO_DATABASE_COMPONENT_NAME)


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

    environment = DiscordListenerEnvironment(properties_holder)
    locator.load(_ENV_COMPONENT_NAME, environment)

    locator.load(_C3PO_VALIDATOR_COMPONENT_NAME, C3POValidator(environment))
    locator.load(
        _MONGO_DATABASE_COMPONENT_NAME, database_client.mongo_init(properties_holder)
    )
