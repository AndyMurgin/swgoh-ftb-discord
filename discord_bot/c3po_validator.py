from discord import Message
from discord.embeds import Embed

from environment import is_tracking_c3po_tb, is_tracking_c3po_tw
from interaction_types import InteractionTypes


def is_valid_tb_gp_low(message: Message):
    return len(message.embeds) == 1 and is_tracking_c3po_tb(message.channel.id)


def is_not_joined_embed(embed: Embed):
    return embed and embed.description and "players not joined" in embed.description


def is_valid_tw_member(message: Message):
    if not message.embeds or len(message.embeds) != 1:
        return False

    return next(
        filter(is_not_joined_embed, message.embeds), None
    ) is not None and is_tracking_c3po_tw(message.channel.id)


def not_to_process(message: Message):
    return False


class C3POValidator:
    __c3po_id = 752366060312723546

    __validators = {
        InteractionTypes.TB_GP_LOW: is_valid_tb_gp_low,
        InteractionTypes.TW_JOIN_STATUS: is_valid_tw_member,
        InteractionTypes.OTHER: not_to_process,
    }

    @staticmethod
    def is_message_to_process(message: Message, type: InteractionTypes) -> bool:
        return (
            message
            and message.author
            and message.author.id == C3POValidator.__c3po_id
            and C3POValidator.__validators[type](message)
        )
