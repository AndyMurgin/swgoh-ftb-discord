from discord import Member
from discord.ext.commands import Context

from environment import is_no_tag_mode


class Notifier:
    @staticmethod
    async def notify_members(ctx: Context, found_members: dict[Member]):
        if Notifier.__is_silent_mode(ctx.channel.id):
            await ctx.send(
                "Режим 'Без Тегов' активирован. Сообщу только имена участников канала"
            )

        await ctx.send(
            "\n".join(
                [
                    Notifier.__get_member_mention(member, ctx.channel.id)
                    for nickname, member in found_members.items()
                ]
            )
        )

    @staticmethod
    async def send_just_nicknames(ctx: Context, nicknames: list[str]):
        await ctx.send(
            "Не смог найти некоторых тюленей в этом канале. Добавьте их вручную (пока не реализовано) "
            "или идите за ними в Telegram:"
        )
        await ctx.send("\n".join([nickname for nickname in nicknames]))

    @staticmethod
    def __get_member_mention(member: Member, channel_id: int):
        return (
            member.display_name
            if Notifier.__is_silent_mode(channel_id)
            else member.mention
        )

    @staticmethod
    def __is_silent_mode(channel_id: int):
        return is_no_tag_mode(channel_id)
