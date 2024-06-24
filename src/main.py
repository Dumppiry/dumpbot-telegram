import logging
from telegram.ext import ApplicationBuilder
from util import config, Logger, parse_args
from handlers import SystemMessageHandler, CleanMessagesHandler


if __name__ == "__main__":
    args = parse_args()
    logger = Logger.create_logger()
    logger.info("Starting bot...")
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handlers(
        [
            SystemMessageHandler,
        ]
    )
    logger.info("Bot started.")
    try:
        app.run_polling()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise e
