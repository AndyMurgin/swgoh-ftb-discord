from discord import Message
from discord.embeds import Embed


def get_not_joined_embed(message: Message) -> Embed | None:
    if not message.embeds or len(message.embeds) == 0:
        return None

    return next(filter(is_not_joined_embed, message.embeds), None)


def is_not_joined_embed(embed: Embed):
    return embed and embed.description and "players not joined" in embed.description
