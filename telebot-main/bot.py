from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5433247438:AAHbxiQXss3uWmey8z8dTkv5h5Fs8oXo_qc",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hi    , Welcome to the CUBE  Bot.Please write\
		/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/hi - greetins
	/website - TECHNICALHAYDEN PORTFOLIO
	/cubevision  - A.I BASED OBJECT DECTION AND IMAGE RECOGNISATION
	/tutorials - GET UNLIMITED TECH TUTORIALS
	/github - TECHNICAL HAYDEN GITHUB PAGES""")

def hi_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"hi  (hi \
		how are you doing)")

def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Your gmail link here (I am not\
		giving mine one for security reasons)")



def website_url(update: Update, context: CallbackContext):
	update.message.reply_text("TECHNICAL HAYDEN PORTFOLIO =>\
	http://technicalhayden.cf/")


def cubevision_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"cube vision A.I => \
		https://technicalhayden.github.io/cubevision/")


def github_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		" GITHUB PAGE  => https://github.com/technicalhayden")


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(CommandHandler('hi', hi_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('cubevision', cubevision_url))
updater.dispatcher.add_handler(CommandHandler('tutorials', gmail_url))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
