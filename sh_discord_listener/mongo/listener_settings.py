from sh_mongo.database_client import MongoDatabase


class ListenerSettingsService:
    __SETTINGS_COLLECTION = "bot_settings"
    __TRACK_C3PO_TB_SETTING = "track_c3po_tb"
    __TRACK_C3PO_TW_SETTING = "track_c3po_tw"

    def __init__(self, db: MongoDatabase):
        self.db = db

    def get_track_c3po_tb_setting(self, channel_id: int) -> bool:
        return self.get_setting_value(channel_id, self.__TRACK_C3PO_TB_SETTING)

    def get_track_c3po_tw_setting(self, channel_id: int) -> bool:
        return self.get_setting_value(channel_id, self.__TRACK_C3PO_TW_SETTING)

    def get_setting_value(self, channel_id: int, setting_name: str):
        found_document = self.db[self.__SETTINGS_COLLECTION].find_one(
            {f"{setting_name}.channel_id": channel_id},
            {"_id": 0, f"{setting_name}.value": 1},
        )
        return (
            found_document
            if found_document is None
            else (found_document.get(setting_name, {}).get("value", None))
        )
