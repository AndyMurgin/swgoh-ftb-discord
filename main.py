import discord
from discord import Message
from discord.ext import commands

from account_sender import OwnerAccountSender
from configs import PropertiesHolder

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
ownerSender = OwnerAccountSender(PropertiesHolder.get_owner_token())


@client.event
async def on_ready():
    print("Go Fight TB!")
    print("-----------------")


@client.event
async def on_message(message):
    await client.process_commands(message)


@client.event
async def on_message_edit(before, after: Message):
    if (
        not after.author.id == 752366060312723546
        or not after.author.name == "C3PO"
        or not after.interaction
        or not after.interaction.name == "tb gp low"
        or not len(after.embeds) == 1
    ):
        return

    seals = [x.name for x in after.embeds[0].fields]
    ctx = await client.get_context(after)
    await ctx.send("WTF??? Быстро бить ТБ!")
    await ctx.send("\n".join(seals))

    await client.process_commands(after)


@client.command()
async def tb(ctx):
    await ctx.send("Capturing the creator's mind...")
    ownerSender.command()


client.run(PropertiesHolder.get_bot_token())
