from discord.ext import commands
from src.util.logger import Logger

class GuildRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = Logger(self.bot)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        self.logger.info(f"The bot left the guild {guild.name} ({guild.id}).")
        await self.logger.discord_log(f"The bot left the guild {guild.name} ({guild.id}).")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GuildRemove(bot))
    return Logger().info("On guild leave event registered!")