import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from Logic_Back_end import add_or_get_user, add_habit_to_user_list, get_all_habits, get_user_habits

TOKEN = '6795112102:AAFBiEZg3Jgi2XxAoqsJvLzUGfSsmvNempo'
bot = telebot.TeleBot(TOKEN)

def generate_markup(habits, page=0):
    markup = types.InlineKeyboardMarkup()
    start_index = page * 10
    end_index = min(start_index + 10, len(habits))
    for habit_id, habit_name in habits[start_index:end_index]:
        button = types.InlineKeyboardButton(habit_name, callback_data=f'add_{habit_id}')
        markup.add(button)

    if start_index > 0:
        markup.add(types.InlineKeyboardButton("⬅️ Назад", callback_data=f'page_{page - 1}'))
    if end_index < len(habits):
        markup.add(types.InlineKeyboardButton("Вперед ➡️", callback_data=f'page_{page + 1}'))

    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    if username is None:
        bot.reply_to(message, "Ваш аккаунт Telegram не имеет username. Пожалуйста, установите его.")
        return

    user_id = add_or_get_user(username)
    welcome_text = "Добро пожаловать! Вот основные команды, которые вы можете использовать:"
    markup = types.InlineKeyboardMarkup(row_width=2)
    commands_buttons = [
        types.InlineKeyboardButton("Просмотр всех привычек", callback_data='all_habits'),
        types.InlineKeyboardButton("Просмотр моих привычек", callback_data='list_habits'),
        types.InlineKeyboardButton("Добавить новую привычку", callback_data='add_new_habit')
    ]
    markup.add(*commands_buttons)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'all_habits')
def show_all_habits_button(call):
    show_all_habits(call.message)


@bot.callback_query_handler(func=lambda call: call.data == 'add_new_habit')
def add_new_habit_button(call):
    # Эта функция должна быть реализована для начала процесса добавления новой привычки
    bot.send_message(call.message.chat.id, "Функция добавления новой привычки ещё не реализована.")


@bot.message_handler(commands=['allhabits'])
def show_all_habits(message):
    habits = get_all_habits()
    if not habits:
        bot.send_message(message.chat.id, "Список привычек пуст.")
        return
    markup = generate_markup(habits)
    bot.send_message(message.chat.id, "Выберите привычку для добавления:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('add_')) # добовление из списка
def handle_add_habit(call):
    habit_id = int(call.data.split('_')[1])
    user_id = add_or_get_user(call.from_user.username)
    add_habit_to_user_list(user_id, habit_id, "ежедневно")  # Пример частоты
    bot.answer_callback_query(call.id, "Привычка добавлена в ваш список.")
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Привычка добавлена!")

@bot.callback_query_handler(func=lambda call: call.data.startswith('page_')) #листать список списка
def handle_pagination(call):
    page = int(call.data.split('_')[1])
    habits = get_all_habits()
    markup = generate_markup(habits, page)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите привычку для добавления:", reply_markup=markup)


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


bot.polling()
