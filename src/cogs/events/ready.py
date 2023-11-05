import logging
from discord.ext import commands
from src.util.logger import Logger
from src.helper.config import Config

class OnReady(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.config = Config()
        self.logger = Logger(self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.clear()
        self.logger.create_logo(self.config.app_name)
        self.logger.info(f"Logged in as {self.bot.user.name}#{self.bot.user.discriminator}.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OnReady(bot))
    return Logger().info("On ready event registered!")