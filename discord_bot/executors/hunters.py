from discord import Message
from discord.ext.commands import Bot

from discord_bot.interaction_types import InteractionTypes
from tb_hunter import TbHunter
from tw_hunter import TwHunter


def _no_hunt(message: Message):
    pass


class HunterFacade:
    __hunters = {InteractionTypes.OTHER: _no_hunt}

    def __init__(self, client: Bot):
        self.__hunters[InteractionTypes.TB_GP_LOW] = TbHunter(client).hunt
        self.__hunters[InteractionTypes.TW_JOIN_STATUS] = TwHunter(client).hunt

    async def hunt(self, message: Message, type: InteractionTypes):
        await self.__hunters[type](message)
