from mongo.mongo_client import db

ACCOUNT_DISCORD_MAPPING_COLLECTION = "swgoh_account_discord_mapping"
SWGOH_ACCOUNT_NAME = "swgoh_acc_name"
DISCORD_CHANNEL_ID = "channel_id"
DISCORD_MENTION = "mention"


class AccountDiscordMappingDbService:
    @staticmethod
    def add_or_update_discord_mention(swgoh_acc_name, channel_id, discord_mention):
        db[ACCOUNT_DISCORD_MAPPING_COLLECTION].update_one(
            {
                f"{SWGOH_ACCOUNT_NAME}": swgoh_acc_name,
                f"{DISCORD_CHANNEL_ID}": channel_id,
            },
            {"$set": {f"{DISCORD_MENTION}": discord_mention}},
            upsert=True,
        )

    @staticmethod
    def get_discord_mention(channel_id, swgoh_acc_name) -> str:
        found_doc = db[ACCOUNT_DISCORD_MAPPING_COLLECTION].find_one(
            {
                f"{DISCORD_CHANNEL_ID}": channel_id,
                f"{SWGOH_ACCOUNT_NAME}": swgoh_acc_name,
            },
            {"_id": 0, f"{DISCORD_MENTION}": 1},
        )
        return (
            found_doc
            if found_doc is None
            else found_doc.get(f"{DISCORD_MENTION}", None)
        )

    @staticmethod
    def get_discord_mentions(channel_id, swgoh_acc_names: list[str]) -> dict:
        return db[ACCOUNT_DISCORD_MAPPING_COLLECTION].find(
            {
                f"{DISCORD_CHANNEL_ID}": channel_id,
                f"{SWGOH_ACCOUNT_NAME}": {"$in": swgoh_acc_names},
            },
            {"_id": 0, f"{SWGOH_ACCOUNT_NAME}": 1, f"{DISCORD_MENTION}": 1},
        )
