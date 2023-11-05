import discord
from discord.ext import commands
from src.helper.config import Config
from src.manager.logger_factory import LoggerFactory

class Logger:

    def __init__(self, bot: commands.Bot = None):
        self.bot = bot
        self.config = Config()
        self.logger = LoggerFactory().get_logger()

    def __getattr__(self, name):
        """
        Delegate attribute lookup to the Logger instance.
        """
        return getattr(self.logger, name)

    async def discord_log(self, description: str):
        channel = self.bot.get_channel(self.config.logs_channel)
        if channel:
            embed = discord.Embed(title=self.config.app_name, description=f"```{description}```")
            embed.set_thumbnail(url=self.config.app_logo)
            embed.set_image(url=self.config.rainbow_line_gif)
            embed.set_footer(text=f"{self.config.app_name_branded}", icon_url=self.config.app_logo)
            embed.timestamp = self.logger.get_current_timestamp()
            await channel.send(embed=embed)
        else:
            self.logger.error(f"Could not find the logs channel with id {self.config.logs_channel}")

    async def dm_user(self, userid: int, message: str):
        user = await self.bot.fetch_user(userid)
        if user:
            await user.send(message)
        else:
            self.logger.error(f"Could not find the user with id {userid}")
            await self.discord_log(f"Could not find the user with id {userid}")