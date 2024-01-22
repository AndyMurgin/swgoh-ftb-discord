from discord import Message
from discord.ext.commands import Bot

from discord_bot.seals_finder import Finder
from discord_bot.seals_notifier import Notifier
from log import logger


class TbHunter:
    __client: Bot = None

    def __init__(self, client: Bot):
        self.__client = client

    async def hunt(self, message: Message):
        ctx = await self.__client.get_context(message)
        logger.info(
            f"Channel: {ctx.channel.id} ({ctx.channel.name}). Starting search for TB seals."
        )

        seals = [x.name for x in message.embeds[0].fields]
        logger.info(
            f"Channel: {ctx.channel.id} ({ctx.channel.name}). Found {len(seals)} seals."
        )

        if len(seals) > 0:
            grouped_members = Finder.find_seal_members(seals, ctx)
            await ctx.send("WTF??? Идем бить ТБ!")

            if len(grouped_members.auto_found_members) > 0:
                logger.info(
                    f"Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to recognized "
                    f"members."
                )
                await Notifier.notify_members(ctx, grouped_members.auto_found_members)

            if len(grouped_members.mapped_accounts) > 0:
                logger.info(
                    f"Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to mapped accounts"
                )
                await Notifier.notify_mapped_accounts(
                    ctx, grouped_members.mapped_accounts
                )

            if len(grouped_members.unrecognized) > 0:
                logger.info(
                    f"Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to unrecognized "
                    f"members."
                )
                await Notifier.send_not_found_nicknames(
                    ctx, grouped_members.unrecognized
                )

            if len(grouped_members.ignored) > 0:
                logger.info(
                    f"Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to ignored "
                    f"members."
                )
                await Notifier.send_ignored_nicknames(ctx, grouped_members.ignored)

        else:
            await ctx.send("Тюлени не обнаружены. Кажется, я попал не в Tython_LEPV.")

        await self.__client.process_commands(message)
