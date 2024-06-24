import logging


class Logger:

    logger_name = "dumpbot"

    # TODO Parameterize
    @staticmethod
    def create_logger():
        logger = logging.getLogger(Logger.logger_name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    @staticmethod
    def get_logger():
        return logging.getLogger(Logger.logger_name)
