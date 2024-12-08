import telebot
from telebot import types
import random

# Токен вашего бота
TOKEN = "Your token"
# Создание объекта бота
bot = telebot.TeleBot(TOKEN)

sortir=["Установите таймер на 5 минут и попытайтесь отсортировать как можно больше отходов.", "Найдите и соберите 5 различных видов отходов в вашем доме, а затем отсортируйте их."]
nedbez=["На одну неделю откажитесь от пластиковых пакетов и одноразовых предметов."]
comand=["Соберите группу друзей и проведите совместный челендж по сбору и сортировке отходов в парке или на пляже"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я экобот. Напиши /challenges, чтобы начать свой экопуть!")

@bot.message_handler(commands=["challenges"])
def challenges_button(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сортировка", callback_data="sort")
    button2 = types.InlineKeyboardButton("Неделя без чего-то", callback_data="nedb")
    button3 = types.InlineKeyboardButton("Командные", callback_data="cmnd")
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Челенджи:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "sort":
            bot.send_message(call.message.chat.id, random.choice(sortir))
        elif call.data == "nedb":
            bot.send_message(call.message.chat.id, random.choice(nedbez))
        elif call.data == "cmnd":
            bot.send_message(call.message.chat.id, random.choice(nedbez))


bot.infinity_polling()
