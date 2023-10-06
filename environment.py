from configs import PropertiesHolder
from mongo_settings_service import SettingsDbService


def update_no_tag_mode(channel_id: int, value: bool) -> bool:
    return SettingsDbService.update_no_tag_setting(channel_id, value)


def is_no_tag_mode(channel_id: int) -> bool:
    channel_notag = SettingsDbService.get_not_tag_setting(channel_id)
    return (
        channel_notag
        if channel_notag is not None
        else PropertiesHolder.get_default_notag_mode()
    )


def update_track_c3po_tb(channel_id: int, value: bool) -> bool:
    return SettingsDbService.update_track_c3po_tb_setting(channel_id, value)


def is_tracking_c3po_tb(channel_id: int):
    channel_track_tb = SettingsDbService.get_track_c3po_tb_setting(channel_id)
    return (
        channel_track_tb
        if channel_track_tb is not None
        else PropertiesHolder.get_default_track_c3po_tb()
    )
