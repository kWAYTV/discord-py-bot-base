from src.helper.config import Config
from kwslogger import Logger as kwslogger

class LoggerFactory:
    def __init__(self):
        self.config = Config()
        self._logger_instance = None

    def get_logger(self):
        if self._logger_instance is None:
            # Initialize the logger instance only once
            self._logger_instance = kwslogger(
                log_level=self.config.log_level,
                log_to_file=self.config.log_to_file,
                log_file_name=self.config.log_file_name,
                log_file_mode=self.config.log_file_mode
            )
        return self._logger_instance