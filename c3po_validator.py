from discord import Message

from environment import ENV


class C3POValidator:
    @staticmethod
    def is_valid_tb_gp_low(message: Message):
        return (
            message.author.id == 752366060312723546
            and message.interaction
            and message.interaction.name == "tb gp low"
            and len(message.embeds) == 1
            and ENV.is_tracking_c3po_tb(message.channel.id)
        )
