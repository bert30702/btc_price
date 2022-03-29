#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://git.io/JOmFw.
"""
import logging
import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

from conversation import keyboard, args, update_bidask

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


yeee = {}

def start(update: Update, context: CallbackContext) -> None:
    # print('CallbackContext:', CallbackContext)
    """Sends a message with three inline buttons attached."""
    
    update_bidask()
    reply_markup = InlineKeyboardMarkup(keyboard['welcome'])
    update.message.reply_text('Start')
    update.message.reply_text('Welcome', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # print('message id:', query.message.reply_to_message.message_id, query.message.reply_to_message.message_id in yeee)
    # yeee[query.message.reply_to_message.message_id] = True
    

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    update_bidask()

    print('Response:', query.data)
    # print(query)

    data = query.data
    print(data)

        
    markup = InlineKeyboardMarkup(keyboard[data])
    query.edit_message_text(args[data], reply_markup=markup) # text=f"Selected option: {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def bert(update: Update, context: CallbackContext) -> None:
    # print('CallbackContext:', CallbackContext)
    """Sends a message with three inline buttons attached."""


    update.message.reply_text('Handsome!')
    # update.message.reply_text('Welcome', reply_markup=reply_markup)


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater('5241169293:AAEj8-zWJ5n0piwv98n3nKpniL3aQSpu7co')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(CommandHandler('bert', bert))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
