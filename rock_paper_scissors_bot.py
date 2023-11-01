import telebot
import random
from telebot import types

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    # Добавляем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # TODO добавить 3 объекта KeyboardButton для 'Камень','Ножницы','Бумага'
    button1 = types.KeyboardButton('🪨')
    button2 = types.KeyboardButton('✂️')
    button3 = types.KeyboardButton('📄')

    # TODO добавить кнопки в клавиатуру (markup)
    markup.add(button1, button2, button3)

    bot.send_message(m.chat.id, 'Нажми кнопку и начни игру ', reply_markup=markup)

# вводим переменные для подсчета общего счета
human_counter = 0
machine_counter = 0


@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Действия при нажатии на кнопки
    machine_list = ['🪨', '✂️', '📄']
    machine_answer = random.choice(machine_list)

    global human_counter
    global machine_counter

    # анализ игры
    if message.text == '🪨':

        # TODO посылать в чат случайное из списка 'Камень','Ножницы','Бумага'
        bot.reply_to(message, machine_answer)

        if machine_answer == '✂️':

            human_counter += 1
            bot.send_message(message.chat.id, 'Ты выиграл!')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')

        elif machine_answer == '📄':

            machine_counter += 1
            bot.send_message(message.chat.id, 'Ты проиграл!')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')

        elif machine_answer == '🪨':
            bot.send_message(message.chat.id, 'Ничья 🤜🤛')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')

    if message.text == '✂️':

        bot.reply_to(message, machine_answer)
        
        if machine_answer == '📄':

            human_counter += 1
            bot.send_message(message.chat.id, 'Ты выиграл!')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')

        elif machine_answer == '🪨':

            machine_counter += 1
            bot.send_message(message.chat.id, 'Ты проиграл!')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')

        elif machine_answer == '✂️':
            bot.send_message(message.chat.id, 'Ничья 🤜🤛')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')

    if message.text == '📄':

        bot.reply_to(message, machine_answer)

        if machine_answer == '🪨':

            human_counter += 1
            bot.send_message(message.chat.id, 'Ты выиграл!')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')

        elif machine_answer == '✂️':

            machine_counter += 1
            bot.send_message(message.chat.id, 'Ты проиграл!')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')

        elif machine_answer == '📄':
            bot.send_message(message.chat.id, 'Ничья 🤜🤛')
            bot.send_message(message.chat.id, f'Общий счет игры: человек: {human_counter} | машина: {machine_counter}')


bot.polling(none_stop=True, interval=0)