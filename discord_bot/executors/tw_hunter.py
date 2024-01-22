from discord import Message
from discord.ext.commands import Bot


class TwHunter:
    __client: Bot = None

    def __init__(self, client: Bot):
        self.__client = client

    def hunt(self, message: Message):
        pass
