from log import logger
from mongo.mongo_accounts_service import (
    ACCOUNT_DISCORD_MAPPING_COLLECTION,
    SWGOH_ACCOUNT_NAME,
    DISCORD_CHANNEL_ID,
)
from mongo.mongo_client import db


def execute():
    logger.info(f"Starting MongoDB initialization - database: {db.name}")

    idx = db[ACCOUNT_DISCORD_MAPPING_COLLECTION].create_index(
        [SWGOH_ACCOUNT_NAME, DISCORD_CHANNEL_ID], unique=True
    )
    logger.info(f"Created index {idx}")

    logger.info(f"Successfully completed MongoDB initialization - database: {db.name}")
