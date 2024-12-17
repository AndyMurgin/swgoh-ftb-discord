from discord_listener_properties import DiscordListenerPropertiesHolder
from sh_discord_listener.mongo.listener_settings import ListenerSettingsService


class DiscordListenerEnvironment:
    def __init__(
        self,
        properties_holder: DiscordListenerPropertiesHolder,
        settings_service: ListenerSettingsService,
    ):
        self.properties_holder = properties_holder
        self.settings_service = settings_service

    def is_tracking_c3po_tb(self, channel_id: int) -> bool:
        channel_track_tb = self.settings_service.get_track_c3po_tb_setting(channel_id)
        return (
            channel_track_tb
            if channel_track_tb is not None
            else self.properties_holder.get_default_track_c3po_tb()
        )

    def is_tracking_c3po_tw(self, channel_id: int) -> bool:
        channel_track_tw = self.settings_service.get_track_c3po_tw_setting(channel_id)
        return (
            channel_track_tw
            if channel_track_tw is not None
            else self.properties_holder.get_default_track_c3po_tw()
        )
