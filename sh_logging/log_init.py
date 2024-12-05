import logging.config
import os

import yaml


def init_logger(logger_name: str, configs_file: str):
    with open(configs_file) as config_file:
        config = yaml.safe_load(config_file.read())
        __create_folders_and_files(config)
        logging.config.dictConfig(config)

    return logging.getLogger(logger_name)


def __create_folders_and_files(config: dict):
    filenames = __get_log_filename(config)
    for filename in filenames or []:
        os.makedirs(os.path.dirname(filename), exist_ok=True)


def __get_log_filename(config: dict) -> list | None:
    return (
        None
        if not config or not config["handlers"]
        else [
            val["filename"] for key, val in config["handlers"].items() if key == "file"
        ]
    )
