import telebot
from telebot import types

bot = telebot.TeleBot('5991103098:AAHlPTkB3pPEDL-63jIAAxBzCN2DSPC0b5g')

managerContact = 'С нетерпением ждy вашего сообщения @werqeeww'

helloMessage = 'Здравствуйте, если вас заинтересовали наши услуги, этот бот содержит ответы на ваши вопросы'

req = '''📌Только граждане РФ🇷🇺, кроме Крыма и Кавказа\n
📌Возраст от 23 лет🙍‍♂️\n
📌Кредитный рейтинг 600+🔝\n
📌Отсутствие просрочек и Микрозаймов🚫'''

faq = '''🔸С какими банками мы работаем?\n
 --Все крупные банки РФ: Сбербанк, ВТБ, Альфа-Банк\n
 \n🔸Сколько времени занимает процесс?\n
 --2-3 недели
 '''

@bot.message_handler(commands=['start'])
def sendMessage(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Требования к заемщику', callback_data='requirements'))
    markup.add(types.InlineKeyboardButton('Частые вопросы', callback_data='faq'))
    markup.add(types.InlineKeyboardButton('Проверить Кредитный Рейтинг',url='https://credistory.ru/'))
    markup.add(types.InlineKeyboardButton('Связаться с нами', callback_data='manager'))
    bot.send_message(message.chat.id,helloMessage,reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'requirements':
        bot.send_message(callback.message.chat.id, req)
    elif callback.data == 'faq':
        bot.send_message(callback.message.chat.id, faq)
    elif callback.data == 'manager':
        bot.send_message(callback.message.chat.id, managerContact)

bot.polling(none_stop=True)