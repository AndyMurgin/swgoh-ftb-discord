import discord
from discord.ext import commands
from configs import PropertiesHolder

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Go Fight TB!")
    print("-----------------")


@client.command()
async def tb(ctx):
    await ctx.send("Go Fight TB, Seal!!!")


client.run(PropertiesHolder.get_bot_token())
