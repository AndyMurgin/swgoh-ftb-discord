import discord
from discord import Message
from discord.ext import commands
from discord.ext.commands import Context

from account_sender import OwnerAccountSender
from c3po_validator import C3POValidator
from configs import PropertiesHolder
from environment import ENV
from seals_finder import Hunter
from seals_notifier import Notifier

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
ownerSender = OwnerAccountSender(PropertiesHolder.get_owner_token())


@client.event
async def on_ready():
    print("Go Fight TB!")
    print("-----------------")


@client.event
async def on_message_edit(before, after: Message):
    if not C3POValidator.is_valid_tb_gp_low(after):
        return

    seals = [x.name for x in after.embeds[0].fields]
    ctx = await client.get_context(after)

    if len(seals) > 0:
        grouped_members = Hunter.find_seal_members(seals, ctx)
        await ctx.send("WTF??? Быстро бить ТБ!")
        if len(grouped_members.found_members) > 0:
            await Notifier.notify_members(ctx, grouped_members.found_members)

        if len(grouped_members.unrecognized) > 0:
            await Notifier.send_just_nicknames(ctx, grouped_members.unrecognized)

    else:
        await ctx.send("Тюлени не обнаружены. Кажется, я попал не в Tython_LEPV.")

    await client.process_commands(after)


@client.command()
async def notag(ctx: Context, value: bool):
    channel_id = ctx.channel.id
    ENV.update_notag_mode(channel_id, value)
    await ctx.send(
        f"Режим 'Без Тегов' {'активирован' if value else 'выключен'} для текущего канала!"
    )


client.run(PropertiesHolder.get_bot_token())
