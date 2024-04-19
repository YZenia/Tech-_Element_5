import telebot
from Logic_Back_end import connect_to_db, add_or_get_user, add_custom_habit, remove_user_habit, list_habits, habit_exists

TOKEN = '6795112102:AAFBiEZg3Jgi2XxAoqsJvLzUGfSsmvNempo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = add_or_get_user(message.from_user.id)
    bot.reply_to(message, "Добро пожаловать! Используйте команды /addhabit, /removehabit или /listhabits для управления привычками.")

@bot.message_handler(commands=['addhabit'])
def add_habit(message):
    msg = bot.send_message(message.chat.id, "Введите название привычки, описание и частоту напоминаний в формате: название;описание;частота")
    bot.register_next_step_handler(msg, process_add_habit)

def process_add_habit(message):
    try:
        habit_name, description, frequency = message.text.split(';')
        user_id = add_or_get_user(message.from_user.id)
        add_custom_habit(user_id, habit_name, description, frequency)
        bot.send_message(message.chat.id, "Привычка успешно добавлена!")
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка формата. Пожалуйста, введите данные в правильном формате.")

@bot.message_handler(commands=['removehabit'])
def remove_habit(message):
    msg = bot.send_message(message.chat.id, "Введите название привычки, которую хотите удалить:")
    bot.register_next_step_handler(msg, process_remove_habit)

def process_remove_habit(message):
    user_id = add_or_get_user(message.from_user.id)
    habit_name = message.text.strip()
    if habit_exists(user_id, habit_name):
        remove_user_habit(user_id, habit_name)
        bot.send_message(message.chat.id, "Привычка удалена.")
    else:
        bot.send_message(message.chat.id, "Привычка с таким названием не найдена.")

@bot.message_handler(commands=['listhabits'])
def list_available_habits(message):
    habits = list_habits()
    habit_list = "\n".join([habit for habit in habits])
    bot.send_message(message.chat.id, "Доступные привычки:\n" + habit_list)

bot.polling()
