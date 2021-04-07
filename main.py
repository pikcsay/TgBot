from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler

TOKEN = ''


def start(update, context):
    update.message.reply_text(
        "Привет! Я бот-помощник в обучении английского языка.")


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только родился.")


def take_words():
    pass


def control_tasks():
    pass


def quests():
    pass


class Vocabulary:
    pass


class RegulEng:
    pass


class SpokenEng:
    pass


if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    updater.start_polling()

    updater.idle()
