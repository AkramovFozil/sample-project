# Importing necessary libraries
from telegram.ext import Application, CommandHandler, MessageHandler, filters

import logging

# Setting up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# Function to start the bot
async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Movie Uploader Bot!")


# Function to upload movies
async def upload_movie(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Please upload the movie file.")


# Function to play movies after joining 5 channels
async def play_movie(update, context):
    chat_members_count = await context.bot.get_chat_member_count(update.effective_chat.id)
    if chat_members_count >= 5:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Enjoy watching the movie!")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Please join at least 5 channels to play movies.")


# Setting up the Telegram Bot
application = Application.builder().token('6341460821:AAFrP1V5oBu7r69d8e3b_xDWXAM-PvTAQBc').build()

# Command handlers
start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

upload_handler = CommandHandler('upload', upload_movie)
application.add_handler(upload_handler)

play_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), play_movie)
application.add_handler(play_handler)

# Starting the bot
application.run_polling()


if __name__ == "__main__":
    application.run_polling()
