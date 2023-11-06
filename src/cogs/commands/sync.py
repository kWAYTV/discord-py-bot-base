from discord.ext import commands
from src.util.logger import Logger
from src.helper.config import Config

class SyncCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.config = Config()
        self.logger = Logger(self.bot)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sync(self, ctx: commands.Context):
        try:
            await ctx.message.delete()
        except:
            self.logger.warning("Tried to delete a message that was not found.")
            pass

        try:
            await self.bot.tree.sync()
            success_message = "✅ Successfully synced slash commands!"
            msg = await ctx.send(success_message)
            
            await self.logger.discord_log(success_message)
            self.logger.info("Slash commands were synced by an admin.")

            # Delete the success message after a delay
            await msg.delete(delay=5)

        except Exception as e:
            error_message = f"❌ Failed to sync slash commands: {e}"
            await ctx.send(error_message, delete_after=10)  # Optionally delete the error message after a delay
            self.logger.error(error_message)

async def setup(bot: commands.Bot):
    await bot.add_cog(SyncCommand(bot))
    Logger().info("Sync command loaded!")