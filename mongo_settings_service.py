from mongo import db


class SettingsDbService:

    @staticmethod
    def update_notag_setting(channel_id: int, value: bool) -> bool:
        db["bot_settings"].update_one({"no_tag.channel_id": channel_id}, {"$set": {"no_tag.value": value}},
                                      upsert=True)
        after_update = db["bot_settings"].find_one({"no_tag.channel_id": channel_id}, {"_id": 0, "no_tag.value": 1})
        return after_update.get("no_tag", {}).get("value", None)

