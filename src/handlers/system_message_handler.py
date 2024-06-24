from util import Logger
from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters


async def HandleSystemMessage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger = Logger.get_logger()
    is_success = await context.bot.delete_message(
        chat_id=update.message.chat_id, message_id=update.message.message_id
    )
    if is_success:
        logger.info(f"System message {update.message.message_id} deleted.")
    else:
        logger.error(
            f"System message {update.message.message_id} could not be deleted."
        )


SystemMessageHandler = MessageHandler(filters.StatusUpdate.ALL, HandleSystemMessage)
