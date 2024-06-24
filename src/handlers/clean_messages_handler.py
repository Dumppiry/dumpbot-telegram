from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, filters
from util import Logger


# TODO Deprecated. Remove this handler.
async def HandleCleanMessages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger = Logger.get_logger()
    logger.info("Cleaning messages")
    chat = await context.bot.get_chat(update.message.chat_id)
    chat.delete_messages()
    print(update.message)
    context.bot.forum
    await context.bot.delete_message(
        chat_id=chat.id, message_id=update.message.message_id
    )


CleanMessagesHandler = CommandHandler("clean", HandleCleanMessages)
