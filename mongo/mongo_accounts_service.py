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
