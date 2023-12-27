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
    async def notify_mapped_accounts(ctx: Context, mapped_accounts: dict):
        if Notifier.__is_silent_mode(ctx.channel.id):
            await ctx.send(
                "Режим 'Без Тегов' активирован. Я знаю следующих тюленей, но не буду их тегать:"
            )

        await ctx.send(
            "\n".join(
                [
                    Notifier.__get_mapped_account_mention(
                        ctx.channel.id, nickname, mention
                    )
                    for (nickname, mention) in mapped_accounts.items()
                ]
            )
        )

    @staticmethod
    async def send_just_nicknames(ctx: Context, nicknames: list[str]):
        await ctx.send(
            "Не смог найти некоторых тюленей в этом канале. Добавьте их вручную (map_mention) "
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
    def __get_mapped_account_mention(
        channel_id: int, account_name: str, mapped_mention: str
    ):
        return account_name if Notifier.__is_silent_mode(channel_id) else mapped_mention

    @staticmethod
    def __is_silent_mode(channel_id: int):
        # TODO need caching
        return is_no_tag_mode(channel_id)
