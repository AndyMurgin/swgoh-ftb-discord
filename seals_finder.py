from discord.ext.commands import Context

from mongo.mongo_accounts_service import (
    AccountDiscordMappingDbService,
    SWGOH_ACCOUNT_NAME,
    DISCORD_MENTION,
)


class SealMembers:
    auto_found_members = {}
    mapped_accounts = {}
    unrecognized = []


class Hunter:
    @staticmethod
    def find_seal_members(seals: list[str], ctx: Context) -> SealMembers:
        grouped_members = SealMembers()
        channel_members = ctx.channel.members
        grouped_members.auto_found_members = {
            nickname: member
            for nickname in seals
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
            for nickname in seals
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
