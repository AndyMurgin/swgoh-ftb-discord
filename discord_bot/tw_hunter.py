from discord import Message
from discord.ext.commands import Bot, Context

import message_utils
from log import logger
from seals_finder import Finder, SealMembers
from seals_notifier import Notifier


class TwHunter:
    __client: Bot = None

    def __init__(self, client: Bot):
        self.__client = client

    async def hunt(self, message: Message):
        ctx = await self.__client.get_context(message)
        logger.info(
            f"TW Search: Channel: {ctx.channel.id} ({ctx.channel.name}). Starting search for not joined TW seals."
        )

        not_joined_members = self.__get_not_joined_list(message)
        logger.info(
            f"TW Search: Channel: {ctx.channel.id} ({ctx.channel.name}). Found {len(not_joined_members)} seals."
        )

        if len(not_joined_members) > 0:
            grouped_members = Finder.find_seal_members(not_joined_members, ctx)
            await self.__notify_seals(ctx, grouped_members)
        else:
            await ctx.send("Тюлени не обнаружены. Кажется, я попал не в Tython_LEPV.")

        await self.__client.process_commands(message)

    def __get_not_joined_list(self, message: Message) -> list[str]:
        not_joined_embed = message_utils.get_not_joined_embed(message)
        # TODO get get text with accounts and parse it to list

    async def __notify_seals(self, ctx: Context, grouped_members: SealMembers):
        await ctx.send("Регистрируемся на ВГ!")
        # TODO picture "are you enlisted?" or "Родина мать зовет"

        if len(grouped_members.auto_found_members) > 0:
            logger.info(
                f"TW Search: Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to recognized "
                f"members ({len(grouped_members.auto_found_members)})."
            )
            await Notifier.notify_members(ctx, grouped_members.auto_found_members)

        if len(grouped_members.mapped_accounts) > 0:
            logger.info(
                f"TW Search: Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to mapped accounts "
                f"({len(grouped_members.mapped_accounts)})"
            )
            await Notifier.notify_mapped_accounts(ctx, grouped_members.mapped_accounts)

        if len(grouped_members.unrecognized) > 0:
            logger.info(
                f"TW Search: Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to unrecognized "
                f"members ({len(grouped_members.unrecognized)})."
            )
            await Notifier.send_not_found_nicknames(ctx, grouped_members.unrecognized)

        if len(grouped_members.ignored) > 0:
            logger.info(
                f"TW Search: Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to ignored "
                f"members ({len(grouped_members.ignored)})."
            )
            await Notifier.send_ignored_nicknames(ctx, grouped_members.ignored)
