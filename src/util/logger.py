import logging
from logging.handlers import RotatingFileHandler


class Logger:

    logger_name = "dumpbot"

    # TODO Parameterize
    @staticmethod
    def create_logger():
        logger = logging.getLogger(Logger.logger_name)
        logger.setLevel(logging.INFO)
        handler = RotatingFileHandler(
            filename="dumpbot.log", maxBytes=2000000, backupCount=10
        )
        print_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s]: %(message)s"
        )
        print_handler.setFormatter(formatter)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.addHandler(print_handler)
        return logger

    @staticmethod
    def get_logger():
        return logging.getLogger(Logger.logger_name)
