from discord import Message
from discord.ext.commands import Bot

from discord_bot.interaction_types import InteractionTypes
from tb_hunter import TbHunter
from tw_hunter import TwHunter


async def _no_hunt(message: Message):
    pass


class HunterFacade:
    _hunters = {InteractionTypes.OTHER.name: _no_hunt}

    def __init__(self, client: Bot):
        self._hunters[InteractionTypes.TB_GP_LOW.name] = TbHunter(client).hunt
        self._hunters[InteractionTypes.TW_JOIN_STATUS.name] = TwHunter(client).hunt

    async def hunt(self, message: Message, type: InteractionTypes):
        await self._hunters[type.name](message)
