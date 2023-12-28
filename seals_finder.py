from discord.ext.commands import Context

from mongo.mongo_accounts_service import (
    AccountDiscordMappingDbService,
    SWGOH_ACCOUNT_NAME,
    DISCORD_MENTION,
)
from mongo.mongo_settings_service import SettingsDbService


class SealMembers:
    auto_found_members = {}
    mapped_accounts = {}
    unrecognized = []
    ignored = []


class Hunter:
    @staticmethod
    def find_seal_members(seals: list[str], ctx: Context) -> SealMembers:
        need_ignore = SettingsDbService.get_ignore_accounts_setting(ctx.channel.id)

        ignored = (
            []
            if need_ignore is None
            else [
                ignore
                for ignore in SettingsDbService.get_ignore_accounts_setting(
                    ctx.channel.id
                )
                if ignore in seals
            ]
        )
        filtered_seals = [seal for seal in seals if seal not in ignored]

        grouped_members = SealMembers()
        grouped_members.ignored = ignored

        channel_members = ctx.channel.members
        grouped_members.auto_found_members = {
            nickname: member
            for nickname in filtered_seals
            for member in channel_members
            if (
                member.display_name.find(nickname)
                if member.display_name is not None
                else -1
            )
            >= 0
        }

        rest_seals = [
            nickname
            for nickname in filtered_seals
            if nickname not in grouped_members.auto_found_members
        ]

        mapped_mentions = AccountDiscordMappingDbService.get_discord_mentions(
            ctx.channel.id, rest_seals
        )
        for mapped_mention in mapped_mentions:
            grouped_members.mapped_accounts[
                mapped_mention[f"{SWGOH_ACCOUNT_NAME}"]
            ] = mapped_mention[f"{DISCORD_MENTION}"]

        grouped_members.unrecognized = [
            nickname
            for nickname in rest_seals
            if nickname not in grouped_members.mapped_accounts
        ]
        return grouped_members
