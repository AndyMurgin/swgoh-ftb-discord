from configs import PropertiesHolder
from mongo.mongo_accounts_service import AccountDiscordMappingDbService
from mongo.mongo_settings_service import SettingsDbService


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


def is_tracking_c3po_tb(channel_id: int) -> bool:
    channel_track_tb = SettingsDbService.get_track_c3po_tb_setting(channel_id)
    return (
        channel_track_tb
        if channel_track_tb is not None
        else PropertiesHolder.get_default_track_c3po_tb()
    )


def is_tracking_c3po_tw(channel_id: int) -> bool:
    channel_track_tw = SettingsDbService.get_track_c3po_tw_setting(channel_id)
    return (
        channel_track_tw
        if channel_track_tw is not None
        else PropertiesHolder.get_default_track_c3po_tw()
    )


def update_discord_to_tele_broadcast(channel_id: int, value: bool) -> bool:
    return SettingsDbService.update_discord_to_tele_broadcast_setting(channel_id, value)


def is_discord_to_tele_broadcast(channel_id: int) -> bool:
    discord_to_tele = SettingsDbService.get_discord_to_tele_broadcast_setting(
        channel_id
    )
    return (
        discord_to_tele
        if discord_to_tele is not None
        else PropertiesHolder.get_default_discord_to_tele_broadcast()
    )


def add_map_mention(channel_id: int, game_nickname: str, discord_mention: str):
    AccountDiscordMappingDbService.add_or_update_discord_mention(
        game_nickname, channel_id, discord_mention
    )


def update_ignore(channel_id: int, game_nickname: str, enabled: bool):
    ignored = SettingsDbService.get_ignore_accounts_setting(channel_id)
    if ignored is None:
        ignored = [game_nickname]

    already_present = game_nickname in ignored
    if enabled and not already_present:
        ignored.append(game_nickname)
    elif not enabled and already_present:
        ignored.remove(game_nickname)

    SettingsDbService.update_ignore_accounts(channel_id, ignored)
