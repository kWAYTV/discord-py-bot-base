from itertools import cycle
from discord.ext import commands
from src.helper.config import Config

class BotStatus:
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.config = Config()

        self.sentences = [
            lambda self: f"Holding {len(self.bot.guilds)} guilds & {sum(guild.member_count for guild in self.bot.guilds)} users.",
            lambda self: f"Hey! My name is {self.config.app_name}.",
        ]

        self.status_generator = cycle(self.sentences)

    async def get_status_message(self) -> str:
        next_status_message = next(self.status_generator)
        return next_status_message(self)