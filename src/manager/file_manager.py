import os
from src.util.logger import Logger
from src.helper.config import Config

defaultConfig = """
## App
app_url: 
app_name: 
app_version: "

## Bot
bot_prefix: 
bot_token: 
logs_channel: 
dev_guild_id: 

## kwslogger
log_level: 
log_to_file: 
log_file_name: 
log_file_mode: 
"""

class FileManager:

    def __init__(self):
        self.logger = Logger()
        self.config = Config()

    # Function to check if the input files are valid
    def check_input(self):

        # if there is no config file, create one.
        if not os.path.isfile("config.yaml"):
            self.logger.info("Config file not found, creating one...")
            open("config.yaml", "w+").write(defaultConfig)
            self.logger.info("Successfully created config.yml, please fill it out and try again.")
            exit()

        # If the folder "/src/database" doesn't exist, create it.
        if not os.path.exists("src/database"):
            os.makedirs("src/database")