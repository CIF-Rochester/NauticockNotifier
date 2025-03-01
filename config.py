from typing import Union, Set
import os
import configparser
import sys
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class API:
    key: str
    channel: str

@dataclass
class Config:
    api: API


def load_config(config_path: os.PathLike) -> Config:
    """
    Load and validate the config file. Exits the program if the config is invalid.
    """
    logger.info(f"Loading config from {config_path}")
    try:
        cfg = configparser.ConfigParser()
        cfg.read(config_path)
    except Exception as e:
        logger.error(f"Failed to load config file from {config_path}", exc_info=e)
        exit(1)

    try:
        api = API(key=cfg.get("api", "key"), channel=cfg.get("api","channel"))

        config = Config(api=api)
        logger.info("Config successfully loaded and parsed")
    except Exception as e:
        logger.error(f"Error in config file {config_path}", exc_info=e)
        exit(1)

    return config
