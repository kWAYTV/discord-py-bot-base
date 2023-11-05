from discord.ext import commands
from src.util.logger import Logger

class GuildJoin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = Logger(self.bot)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        try:
            # Sync the commands
            await self.bot.tree.sync()
        except Exception as e:
            self.logger.error(f"❌ Failed to sync slash commands: {e}")
            await self.logger.discord_log(f"❌ Failed to sync slash commands: {e}")
            return

        # Send a DM to the guild owner
        try:
            await guild.owner.send(f"Hello `{guild.owner.name}`, your guild `{guild.name}` has successfully synced commands with the bot!")
        except:
            self.logger.loinfog(f"❌ Couln't send a DM to the guild owner of {guild.name} ({guild.owner.id}).")
            await self.logger.discord_log(f"❌ Couln't send a DM to the guild owner of {guild.name} ({guild.owner.id}).")
            return
        
        # Log the event
        self.logger.info(f"✅ Bot joined Guild: {guild.name}. ({guild.id})")
        await self.logger.discord_log(f"✅ Bot joined Guild: {guild.name} ({guild.id}).")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GuildJoin(bot))
    return Logger().info("On guild join event registered!")