from configs import PropertiesHolder
from mongo_settings_service import SettingsDbService


class Environment:
    __settings = {}

    def is_notag_mode(self, channel_id: int):
        notag = self.__settings.get("notag")
        channel_notag = notag.get(channel_id) if notag is not None else None
        return (
            channel_notag
            if channel_notag is not None
            else PropertiesHolder.get_default_notag_mode()
        )

    def update_notag_mode(self, channel_id: int, value: bool) -> bool:
        return SettingsDbService.update_notag_setting(channel_id, value)

    def is_tracking_c3po_tb(self, channel_id: int):
        track_tb = self.__settings.get("track_c3po_tb")
        channel_track_tb = track_tb.get(channel_id) if track_tb is not None else None
        return (
            channel_track_tb
            if channel_track_tb is not None
            else PropertiesHolder.get_default_track_c3po_tb()
        )

    def update_track_c3po_tb(self, channel_id: int, value: bool):
        self.__settings.update({"track_c3po_tb": {channel_id: value}})


ENV = Environment()
