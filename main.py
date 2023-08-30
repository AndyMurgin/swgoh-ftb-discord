import discord
from configs import PropertiesHolder
from discord.ext import commands
from account_sender import OwnerAccountSender

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
ownerSender = OwnerAccountSender(PropertiesHolder.get_owner_token())


@client.event
async def on_ready():
    print("Go Fight TB!")
    print("-----------------")


@client.command()
async def tb(ctx):
    await ctx.send("Capturing the creator's mind...")
    ownerSender.command()


client.run(PropertiesHolder.get_bot_token())
