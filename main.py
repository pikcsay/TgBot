import requests
import sqlite3
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import wikipedia as wiki
from newsapi import NewsApiClient
from settings import TOKEN, DB, NEWS_KEY

wiki.set_lang("en")
newsapi = NewsApiClient(api_key=NEWS_KEY)


def start_keyboard(update, context, text, markup):
    update.message.reply_text(text, reply_markup=markup)


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def wiki_info(update, context):
    words = ' '.join(context.args)
    info = wiki.summary("{}".format(words), chars=4096)
    update.message.reply_text('Вот что мне удалось найти по запросу {}:\n{}'.format(words, info))


def get_news(update, context):
    if not context.args or context.args[0] not in ('technology', 'science', 'entertainment', 'general'):
        reply_keyboard = [['/news technology', '/news science'],
                          ['/news entertainment', '/news general']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        start_keyboard(update, context, "Какая тема вас интересует?", markup)
    category = context.args[0]
    k = 10
    top_headlines = newsapi.get_top_headlines(category=category, language='en', country='us')
    if top_headlines['status'] == 'ok':
        if top_headlines['totalResults'] < 7:
            k = top_headlines['totalResults']
        news = top_headlines['articles']
        top_headlines = ['• {}: {}'.format(i['source']['name'], i['title']) for i in news[:k]]
        update.message.reply_text('News:\n' + '\n'.join(top_headlines), reply_markup=ReplyKeyboardRemove())


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


# def translate(update, context):
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
    def __init__(self):
        pass

    def get_regul(self, update, context):
        con = sqlite3.connect(DB)

        cur = con.cursor()
        regul = cur.execute("""SELECT path FROM Regulations WHERE name = ?""", (context.args[0],)).fetchone()[0]
        if regul:
            context.bot.send_photo(
                update.message.chat_id,
                open(regul, 'rb'),
                caption="Нашёл:"
            )


class SpokenEng:
    pass


if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    reg = RegulEng()

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # dp.add_handler(CommandHandler("translate", translate))
    dp.add_handler(CommandHandler("wiki", wiki_info))
    dp.add_handler(CommandHandler('news', get_news))
    dp.add_handler(CommandHandler('reg', reg.get_regul))

    updater.start_polling()

    updater.idle()
