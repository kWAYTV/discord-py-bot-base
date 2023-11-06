# Imports
import discord, os
from discord.ext import commands
from src.util.logger import Logger
from src.helper.config import Config
from src.manager.file_manager import FileManager

# Define the bot & load the commands, events and loops
class Bot(commands.Bot):
    def __init__(self) -> None:
        self.logger = Logger()
        self.file_manager = FileManager()
        super().__init__(command_prefix=Config().bot_prefix, help_command=None, intents=discord.Intents.all())

    # Function to load the extensions
    async def setup_hook(self) -> None:
        self.logger.clear()
        self.logger.info(f"Starting bot...")

        # Check for file inputs
        self.logger.info("Checking for file inputs...")
        self.file_manager.check_input()
        self.logger.clear()

        # Load the cogs
        self.logger.info("Loading cogs...")
        for filename in os.listdir("./src/cogs/commands"):
            if filename.endswith(".py") and not filename.startswith("_"):
                await self.load_extension(f"src.cogs.commands.{filename[:-3]}")
        self.logger.clear()

        # Load the events
        self.logger.info("Loading events...")
        for filename in os.listdir("./src/cogs/events"):
            if filename.endswith(".py") and not filename.startswith("_"):
                await self.load_extension(f"src.cogs.events.{filename[:-3]}")
        self.logger.clear()

        # Load the loops
        self.logger.info("Loading loops...")
        for filename in os.listdir("./src/cogs/loops"):
            if filename.endswith(".py") and not filename.startswith("_"):
                await self.load_extension(f"src.cogs.loops.{filename[:-3]}")
        self.logger.clear()

        # Done!
        self.logger.info(f"Setup completed!")

# Run the bot
if __name__ == "__main__":
    try:
        bot = Bot()
        bot.run(Config().bot_token)
    except KeyboardInterrupt:
        Logger.info("Goodbye!")
        exit()
