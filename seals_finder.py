from discord.ext.commands import Context


class SealMembers:
    found_members = {}
    unrecognized = []


class Hunter:
    @staticmethod
    def find_seal_members(seals: list[str], ctx: Context) -> SealMembers:
        grouped_members = SealMembers()
        channel_members = ctx.channel.members
        grouped_members.found_members = {
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
        grouped_members.unrecognized = [
            nickname
            for nickname in seals
            if nickname not in grouped_members.found_members
        ]
        return grouped_members
