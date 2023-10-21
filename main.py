import discord
from discord import Message
from discord.ext import commands
from discord.ext.commands import Context

from account_sender import OwnerAccountSender
from c3po_validator import C3POValidator
from configs import PropertiesHolder
from environment import update_no_tag_mode, update_track_c3po_tb, add_map_mention
from log import logger
from mongo import mongo_init
from seals_finder import Hunter
from seals_notifier import Notifier

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
ownerSender = OwnerAccountSender(PropertiesHolder.get_owner_token())


@client.event
async def on_ready():
    logger.info("The bot has been started! GO FIGHT TB!")


@client.event
async def on_message_edit(before, after: Message):
    try:
        if not C3POValidator.is_valid_tb_gp_low(after):
            logger.debug("Triggered by not a C3PO")
            return

        ctx = await client.get_context(after)
        logger.info(
            f"Channel: {ctx.channel.id} ({ctx.channel.name}). Starting search for TB seals."
        )

        seals = [x.name for x in after.embeds[0].fields]
        logger.info(
            f"Channel: {ctx.channel.id} ({ctx.channel.name}). Found {len(seals)} seals."
        )

        if len(seals) > 0:
            grouped_members = Hunter.find_seal_members(seals, ctx)
            await ctx.send("WTF??? Быстро бить ТБ!")

            if len(grouped_members.found_members) > 0:
                logger.info(
                    f"Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to recognized "
                    f"members."
                )
                await Notifier.notify_members(ctx, grouped_members.found_members)

            if len(grouped_members.unrecognized) > 0:
                logger.info(
                    f"Channel: {ctx.channel.id} ({ctx.channel.name}). Sending notifications to unrecognized "
                    f"members."
                )
                await Notifier.send_just_nicknames(ctx, grouped_members.unrecognized)

        else:
            await ctx.send("Тюлени не обнаружены. Кажется, я попал не в Tython_LEPV.")

        await client.process_commands(after)
    except Exception as e:
        logger.exception(f"Error during message processing. Message: {after.content}")


@client.command()
async def notag(ctx: Context, value: bool):
    logger.info(
        f"Channel: {ctx.channel.id} ({ctx.channel.name}). Received 'notag' command with value {value}"
    )
    try:
        channel_id = ctx.channel.id
        updated_setting = update_no_tag_mode(channel_id, value)

        if updated_setting is None:
            await setting_update_error(ctx)

        else:
            logger.info(
                f"Channel: {ctx.channel.id} ({ctx.channel.name}). 'notag' value has been changed to "
                f"{updated_setting}"
            )
            await ctx.send(
                f"Режим 'Без Тегов' {'активирован' if updated_setting else 'выключен'} для текущего канала!"
            )

    except Exception as e:
        logger.exception("Error during notag command processing.")


@client.command()
async def track_c3po_tb(ctx: Context, value: bool):
    logger.info(
        f"Channel: {ctx.channel.id} ({ctx.channel.name}). Received 'track_c3po_tb' command with value {value}"
    )
    try:
        channel_id = ctx.channel.id
        updated_setting = update_track_c3po_tb(channel_id, value)

        if updated_setting is None:
            await setting_update_error(ctx)

        else:
            logger.info(
                f"Channel: {ctx.channel.id} ({ctx.channel.name}). 'track_c3po_tb' value has been changed to "
                f"{updated_setting}"
            )
            await ctx.send(
                f"Режим 'Поддержка C3PO В Поиске Тюленей' {'активирован' if updated_setting else 'выключен'} "
                f"для текущего канала!"
            )

    except Exception as e:
        logger.exception("Error during track_c3po_tb command processing.")


@client.command()
async def map_mention(ctx: Context, nickname: str, mention: str):
    channel_str = f"Channel: {ctx.channel.id} ({ctx.channel.name})."
    logger.info(
        f"{channel_str} Received 'map_mention' command with parameters: {nickname}, {mention}"
    )
    try:
        add_map_mention(ctx.channel.id, nickname, mention)

        logger.info(
            f"{channel_str}. 'map_mention' has been processed for nickname {nickname}"
        )
        await ctx.send(
            f"Соответствие добавлено - теперь ты от меня не уйдешь, {mention}!"
        )

    except Exception as e:
        logger.exception("Error during map_mention command processing.")


async def setting_update_error(ctx: Context):
    logger.warning(
        f"Channel: {ctx.channel.id} ({ctx.channel.name}). Unable to update setting value: None"
    )
    await ctx.send(f"Ошибка при сохранении значения в БД! Обратитесь к создателю.")


def __init_mongo_if_required():
    if PropertiesHolder.get_mongo_init():
        mongo_init.execute()


__init_mongo_if_required()
client.run(PropertiesHolder.get_bot_token())
