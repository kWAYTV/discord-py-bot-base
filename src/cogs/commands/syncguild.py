from discord.ext import commands
from src.util.logger import Logger
from src.helper.config import Config

class SyncGuildCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = Config()
        self.logger = Logger(self.bot)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def syncguild(self, ctx: commands.Context):
        try:
            await ctx.message.delete()
        except:
            self.logger.warning("Tried to delete a message that was not found.")
            pass

        try:
            await self.bot.tree.sync(guild=ctx.guild)
            success_message = "✅ Successfully synced guild slash commands!"
            msg = await ctx.send(success_message)
            
            await self.logger.discord_log(success_message)
            self.logger.info("Guild slash commands were synced by an admin.")
        except Exception as e:
            error_message = f"❌ Failed to sync guild slash commands: {e}"
            await ctx.send(error_message)
            self.logger.error(error_message)

        await msg.delete(delay=5)

async def setup(bot: commands.Bot):
    await bot.add_cog(SyncGuildCommand(bot))
    Logger().info("Syncguild command loaded!")
