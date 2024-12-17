import argparse

import discord
from discord import Message
from discord.ext import commands

import dl_service_locator
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

        if not locator.c3po_validator().is_message_to_process(after, interaction_type):
            logger.debug("Unsupported message edit")
            return

        # TODO save a processing request in DB for the message

    except Exception as e:
        logger.exception(f"Error during message processing. Message: {after.content}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("props", nargs="?", default="application.properties", type=str)
    args = parser.parse_args()

    dl_service_locator.configure(args.props)

    global locator
    locator = dl_service_locator.locator
    client.run(locator.properties_holder().get_discord_bot_token())
