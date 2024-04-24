# Импорт модуля pyTelegramBotAPI для создания телеграм-бота
# Импорт types для создания клавиатуры и кнопок в интерфейсе
import telebot
from telebot import types
# Следующая строка не нужна, так как предыдущая уже импортирует нужные классы объектов types
# ??? ЗАПРОС НА УДАЛЕНИЕ ???
# from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
# Импорт функций из файла Python Logic_Back_end.py
from Logic_Back_end import (add_or_get_user,
                            add_habit_to_user_list, get_user_habits, get_new_habits,
                            add_habit_to_user_list_directly)  # get_all_habits

# Ввод токена основного телеграм-бота и инициализация программы:
TOKEN = '6795112102:AAFBiEZg3Jgi2XxAoqsJvLzUGfSsmvNempo'
bot = telebot.TeleBot(TOKEN)

# !!! ПЕРЕКЛЮЧИТЬ НА ОСНОВНОЙ ТЕЛЕГРАМ-БОТ В ФИНАЛЬНОЙ ВЕРСИИ ПРОГРАММЫ !!!

# Ввод токена тестового телеграм-бота и инициализация программы
# TEST_TOKEN = '7088266760:AAG2r0Dz3GJAymtpxqrQpapNgVC91u8E23Q'
# bot = telebot.TeleBot(TEST_TOKEN)


# Функция вызова списка привычек из таблицы 'habits' в виде клавиатуры для выбора пользователя
def generate_markup(habits, page=0, list_type='habits'):
    markup = types.InlineKeyboardMarkup()
    start_index = page * 10
    end_index = min(start_index + 10, len(habits))
    for habit_id, habit_name in habits[start_index:end_index]:
        button = types.InlineKeyboardButton(habit_name, callback_data=f'add_{habit_id}')
        markup.add(button)

    if start_index > 0:
        markup.add(types.InlineKeyboardButton("⬅️ Назад", callback_data=f'page_{page - 1}_{list_type}'))
    if end_index < len(habits):
        markup.add(types.InlineKeyboardButton("Вперед ➡️", callback_data=f'page_{page + 1}_{list_type}'))

    return markup


# Функция-приветствие нового пользователя
@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    if username is None:
        bot.reply_to(message, "Ваш аккаунт Telegram не имеет username. Пожалуйста, установите его.")
        return

    user_id = add_or_get_user(username)
    welcome_text = "Добро пожаловать! Вот основные команды, которые вы можете использовать в боте Привычек:"
    markup = types.InlineKeyboardMarkup(row_width=2)
    commands_buttons = [
        types.InlineKeyboardButton("Добавить свою П.", callback_data='add_new_habit'),
        types.InlineKeyboardButton("Настройка моих П.", callback_data='list_habits'),
        types.InlineKeyboardButton("База Привычек", callback_data='all_habits')
    ]
    markup.add(*commands_buttons)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# Функция по нажатию кнопки "База Привычек":
# вывод всех привычек из таблицы 'habits', кроме уже добавленных в список привычек пользователя;
# с возможностью выбора новой привычки для добавления в список привычек пользователя

# @bot.callback_query_handler(func=lambda call: call.data == 'add_new_habit')
# def show_all_habits_button(call):
#     show_all_habits(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'add_new_habit')
def add_new_habit_button(call):
    # Начало диалога для добавления новой привычки
    msg = bot.send_message(call.message.chat.id, "Введите название новой привычки:")
    bot.register_next_step_handler(msg, process_habit_name_step, user_id=call.from_user.id)


def process_habit_name_step(message, user_id):
    habit_name = message.text
    msg = bot.send_message(message.chat.id, "Введите описание привычки:")
    bot.register_next_step_handler(msg, process_habit_description_step, user_id=user_id, habit_name=habit_name)


def process_habit_description_step(message, user_id, habit_name):
    description = message.text
    msg = bot.send_message(message.chat.id, "Введите цель привычки:")
    bot.register_next_step_handler(msg, process_habit_goal_step, user_id=user_id, habit_name=habit_name,
                                   description=description)


def process_habit_goal_step(message, user_id, habit_name, description):
    goal = message.text
    msg = bot.send_message(message.chat.id, "Введите частоту напоминаний (например, 'ежедневно'):")
    bot.register_next_step_handler(msg, process_habit_frequency_step, user_id=user_id, habit_name=habit_name,
                                   description=description, goal=goal)


def process_habit_frequency_step(message, user_id, habit_name, description, goal):
    frequency = message.text
    username = message.from_user.username
    # Добавляем привычку в базу и связываем её с пользователем
    add_habit_to_user_list_directly(username, user_id, habit_name, description, goal, frequency)
    bot.send_message(message.chat.id, "Привычка успешно добавлена в ваш список.")


# Функция - обработка запроса на вызов функции show_all_habits() - СМ. СТРОКУ 89
@bot.callback_query_handler(func=lambda call: call.data == 'all_habits')
def show_all_habits(call):
    # Эта функция должна быть реализована для начала процесса добавления новой привычки
    # bot.send_message(call.message.chat.id, "Функция добавления новой привычки ещё не реализована.")
    username = call.from_user.username
    if username is None:
        bot.answer_callback_query(call.id, "У вашего профиля в Telegram нет username!")
        return

    user_id = add_or_get_user(username)
    new_habits = get_new_habits(user_id)
    if not new_habits:
        bot.send_message(call.message.chat.id, "Список привычек пуст.")
        return
    markup = generate_markup(new_habits, list_type='newhabits')
    bot.send_message(call.message.chat.id, "Выберите привычку для добавления:", reply_markup=markup)


# Функция - вывод всех привычек из таблицы 'habits' с возможностью выбора
# новой привычки для добавления в список привычек пользователя - СМ. СТРОКУ 61
# @bot.message_handler(commands=['allhabits'])
# def show_all_habits(message):
#     habits = get_all_habits()
#     if not habits:
#         bot.send_message(message.chat.id, "Список привычек пуст.")
#         return
#     markup = generate_markup(habits, list_type='habits')
#     bot.send_message(message.chat.id, "Выберите привычку для добавления:", reply_markup=markup)


# Функция - обработка запроса на добавление пользователю новой привычки из таблицы 'habits'
@bot.callback_query_handler(func=lambda call: call.data.startswith('add_')) # добовление из списка
def handle_add_habit(call):
    habit_id = int(call.data.split('_')[1])
    user_id = add_or_get_user(call.from_user.username)
    add_habit_to_user_list(user_id, habit_id, "ежедневно")  # Пример частоты
    bot.answer_callback_query(call.id, "Привычка добавлена в ваш список.")
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Привычка добавлена!")


# Функция - обработка запроса на перелистывание страниц списка привычек из 'habits'
@bot.callback_query_handler(func=lambda call: call.data.startswith('page_')) #листать список списка
def handle_pagination(call):
    _, page, list_type = call.data.split('_')
    page = int(page)
    if list_type == 'habits':
        pass
        # habits = get_all_habits()
    elif list_type == 'newhabits':
        habits = get_new_habits(call.from_user.username)
    markup = generate_markup(habits, page, list_type)
    bot.edit_message_text(
        chat_id=call.message.chat.id, message_id=call.message.message_id,
        text="Выберите привычку для добавления:", reply_markup=markup
    )


# Функция - обработка запроса на вывод списка привычек пользователя
@bot.callback_query_handler(func=lambda call: call.data == 'list_habits')
def list_user_habits(call):
    username = call.from_user.username
    if username is None:
        bot.answer_callback_query(call.id, "У вашего профиля в Telegram нет username!")
        return

    user_id = add_or_get_user(username)

    # Получение списка привычек пользователя
    habits = get_user_habits(user_id)

    if not habits:
        bot.send_message(call.message.chat.id, "Ваш список привычек пуст.")
        return

    # Формирование текста сообщения со списком привычек
    habits_text = "\n".join(habit_name for _, habit_name in habits)
    bot.send_message(call.message.chat.id, "Ваши привычки:\n" + habits_text)


# Запуск работы телеграм-бота с пользователем
bot.polling()
