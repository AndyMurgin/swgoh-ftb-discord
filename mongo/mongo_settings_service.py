from mongo.mongo_client import db

SETTINGS_COLLECTION = "bot_settings"
NO_TAG_SETTING = "no_tag"
TRACK_C3PO_TB_SETTING = "track_c3po_tb"
TRACK_C3PO_TW_SETTING = "track_c3po_tw"
IGNORE_ACCOUNTS_SETTINGS = "ignore_accounts"


class SettingsDbService:
    @staticmethod
    def update_no_tag_setting(channel_id: int, value: bool) -> bool:
        return SettingsDbService.update_setting_value(channel_id, NO_TAG_SETTING, value)

    @staticmethod
    def get_not_tag_setting(channel_id: int) -> bool:
        return SettingsDbService.get_setting_value(channel_id, NO_TAG_SETTING)

    @staticmethod
    def update_track_c3po_tb_setting(channel_id: int, value: bool) -> bool:
        return SettingsDbService.update_setting_value(
            channel_id, TRACK_C3PO_TB_SETTING, value
        )

    @staticmethod
    def get_track_c3po_tb_setting(channel_id: int) -> bool:
        return SettingsDbService.get_setting_value(channel_id, TRACK_C3PO_TB_SETTING)

    @staticmethod
    def update_track_c3po_tw_setting(channel_id: int, value: bool) -> bool:
        return SettingsDbService.update_setting_value(
            channel_id, TRACK_C3PO_TW_SETTING, value
        )

    @staticmethod
    def get_track_c3po_tw_setting(channel_id: int) -> bool:
        return SettingsDbService.get_setting_value(channel_id, TRACK_C3PO_TW_SETTING)

    @staticmethod
    def update_ignore_accounts(channel_id: int, accounts: list[str]) -> list[str]:
        return SettingsDbService.update_setting_value(
            channel_id, IGNORE_ACCOUNTS_SETTINGS, accounts
        )

    @staticmethod
    def get_ignore_accounts_setting(channel_id: int) -> list[str]:
        return SettingsDbService.get_setting_value(channel_id, IGNORE_ACCOUNTS_SETTINGS)

    @staticmethod
    def update_setting_value(channel_id: int, setting_name: str, value):
        db[SETTINGS_COLLECTION].update_one(
            {f"{setting_name}.channel_id": channel_id},
            {"$set": {f"{setting_name}.value": value}},
            upsert=True,
        )
        return SettingsDbService.get_setting_value(channel_id, setting_name)

    @staticmethod
    def get_setting_value(channel_id: int, setting_name: str):
        found_document = db[SETTINGS_COLLECTION].find_one(
            {f"{setting_name}.channel_id": channel_id},
            {"_id": 0, f"{setting_name}.value": 1},
        )
        return (
            found_document
            if found_document is None
            else (found_document.get(setting_name, {}).get("value", None))
        )
