import discord
from discord import Message
from discord.ext import commands
from discord.ext.commands import Context

from configs import PropertiesHolder
from discord_bot.account_sender import OwnerAccountSender
from discord_bot.c3po_validator import C3POValidator
from discord_bot.hunters import HunterFacade
from environment import (
    update_no_tag_mode,
    update_track_c3po_tb,
    update_discord_to_tele_broadcast,
    add_map_mention,
    update_ignore,
)
from interaction_types import InteractionTypes
from log import logger
from mongo import mongo_init

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
HUNTER = HunterFacade(client)
ownerSender = OwnerAccountSender(PropertiesHolder.get_owner_token())


@client.event
async def on_ready():
    logger.info("The bot has been started! READY TO DEMOLISH!")


@client.event
async def on_message_edit(before, after: Message):
    try:
        interaction_type = InteractionTypes.get_interaction_type(after.interaction)

        if not C3POValidator.is_message_to_process(after, interaction_type):
            logger.debug("Unsupported message edit")
            return

        await HUNTER.hunt(after, interaction_type)

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
async def discord_to_tele(ctx: Context, value: bool):
    logger.info(
        f"Channel: {ctx.channel.id} ({ctx.channel.name}). Received 'discord_to_tele' command with value {value}"
    )
    try:
        channel_id = ctx.channel.id
        updated_setting = update_discord_to_tele_broadcast(channel_id, value)

        if updated_setting is None:
            await setting_update_error(ctx)

        else:
            logger.info(
                f"Channel: {ctx.channel.id} ({ctx.channel.name}). 'discord_to_tele' value has been changed to "
                f"{updated_setting}"
            )
            await ctx.send(
                f"Режим 'Вещание в Telegram' {'активирован' if updated_setting else 'выключен'} "
                f"для текущего канала!"
            )

    except Exception as e:
        logger.exception("Error during discord_to_tele command processing.")


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


@client.command()
async def ignore(ctx: Context, nickname: str, enabled: bool):
    channel_str = f"Channel: {ctx.channel.id} ({ctx.channel.name})."
    logger.info(
        f"{channel_str} Received 'ignore' command with parameters: {nickname}, {enabled}"
    )
    try:
        update_ignore(ctx.channel.id, nickname, enabled)

        logger.info(
            f"{channel_str}. 'ignore' has been processed for nickname {nickname}"
        )
        await ctx.send(
            f"Принято - не буду беспокоить {nickname}"
            if enabled
            else f"Принято - буду снова карать {nickname}"
        )

    except Exception as e:
        logger.exception("Error during ignore command processing.")


async def setting_update_error(ctx: Context):
    logger.warning(
        f"Channel: {ctx.channel.id} ({ctx.channel.name}). Unable to update setting value: None"
    )
    await ctx.send(f"Ошибка при сохранении значения в БД! Обратитесь к создателю.")


def __init_mongo_if_required():
    if PropertiesHolder.get_mongo_init().lower() == "true":
        mongo_init.execute()


__init_mongo_if_required()
client.run(PropertiesHolder.get_discord_bot_token())
