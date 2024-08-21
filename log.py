import logging.config

import yaml

with open("log-configs.yaml") as config_file:
    config = yaml.safe_load(config_file.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("bot-logger")
