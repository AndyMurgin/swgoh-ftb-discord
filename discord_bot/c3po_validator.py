from discord import Message

from environment import is_tracking_c3po_tb
from interaction_types import InteractionTypes


def is_valid_tb_gp_low(message: Message):
    return len(message.embeds) == 1 and is_tracking_c3po_tb(message.channel.id)


def is_valid_tw_member(message: Message):
    return False  # TODO


def not_valid(message: Message):
    return False


class C3POValidator:
    __validators = {InteractionTypes.OTHER: not_valid}

    @staticmethod
    def is_valid_tb_gp_low(message: Message):
        return (
            message.author.id == 752366060312723546
            and message.interaction
            and message.interaction.name == "tb gp low"
            and len(message.embeds) == 1
            and is_tracking_c3po_tb(message.channel.id)
        )
