import discord
from discord import Message
from discord.ext import commands

import dl_service_locator
from dl_service_locator import locator
from sh_discord_utils.interaction_types import InteractionTypes

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    locator.logger().info("The Discord Message Listener has been started")


@client.event
async def on_message_edit(before, after: Message):
    logger = locator.logger()
    try:
        interaction_type = InteractionTypes.get_interaction_type(after.interaction)

        # TODO continue working on c3po_validator
        if not C3POValidator.is_message_to_process(after, interaction_type):
            logger.debug("Unsupported message edit")
            return

    except Exception as e:
        logger.exception(f"Error during message processing. Message: {after.content}")


if __name__ == "__main__":
    dl_service_locator.configure()
    client.run(locator.properties_holder().get_discord_bot_token())
