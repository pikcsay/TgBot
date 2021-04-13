import requests
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import wikipedia as wiki

TOKEN = ''
wiki.set_lang("en")


def wiki_info(update, context):
    words = ' '.join(context.args)
    info = wiki.summary("{}".format(words), chars=4096)
    update.message.reply_text('Вот что мне удалось найти по запросу {}:\n{}'.format(words, info))


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


#def translate(update, context):
#    params = {
#        "key": KEY,
#        "text": ' '.join(context.args),
#        "lang": 'ru-en'
#    }
#    response = requests.get(URL, params=params)
#    update.message.reply_text(response.json()['text'])


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
    #dp.add_handler(CommandHandler("translate", translate))
    dp.add_handler(CommandHandler("wiki", wiki_info))

    updater.start_polling()

    updater.idle()
