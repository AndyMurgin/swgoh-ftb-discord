from discord import Message

from sh_discord_utils import message_utils
from sh_discord_utils.interaction_types import InteractionTypes
from .discord_listener_environment import DiscordListenerEnvironment


class C3POValidator:
    __c3po_id = 752366060312723546

    def __init__(self, environment: DiscordListenerEnvironment):
        self._environment = environment
        self._validators = {
            InteractionTypes.TB_GP_LOW.name: self._is_valid_tb_gp_low,
            InteractionTypes.TW_JOIN_STATUS.name: self._is_valid_tw_member,
            InteractionTypes.OTHER.name: self._not_to_process,
        }

    def is_message_to_process(self, message: Message, type: InteractionTypes) -> bool:
        return (
            message
            and message.author
            and message.author.id == C3POValidator.__c3po_id
            and self._validators[type.name](message)
        )

    def _is_valid_tb_gp_low(self, message: Message):
        return len(message.embeds) == 1 and self._environment.is_tracking_c3po_tb(
            message.channel.id
        )

    def _is_valid_tw_member(self, message: Message):
        return message_utils.get_not_joined_embed(
            message
        ) is not None and self._environment.is_tracking_c3po_tw(message.channel.id)

    def _not_to_process(self, message: Message):
        return False
