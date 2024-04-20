import telebot

from Logic_Back_end import connect_to_db, add_or_get_user, add_custom_habit, remove_user_habit, list_habits, habit_exists

from Logic_Back_end import add_or_get_user, add_habit_to_user, remove_habit_from_user, list_user_habits


TOKEN = '6795112102:AAFBiEZg3Jgi2XxAoqsJvLzUGfSsmvNempo'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = add_or_get_user(message.from_user.id)
    bot.reply_to(message, "Добро пожаловать! Используйте команды /addhabit, /removehabit или /listhabits для управления привычками.")

@bot.message_handler(commands=['addhabit'])
def add_habit(message):
    msg = bot.send_message(message.chat.id, "Введите название привычки, описание и частоту напоминаний в формате: название;описание;частота")
    print(msg)
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

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_id = add_or_get_user(message.from_user.id)
    reply_text = "Добро пожаловать! Используйте /addhabit и /removehabit для управления привычками. Например, введите /addhabit чтобы добавить привычку."
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['addhabit'])
def handle_addhabit(message):
    # Получаем user_id из ID пользователя Telegram
    user_id = add_or_get_user(message.from_user.id)
    habit_name = "Здоровое питание"  # Здесь можно динамически запросить название привычки от пользователя
    add_habit_to_user(user_id, habit_name)
    bot.reply_to(message, f"Привычка '{habit_name}' добавлена для вашего аккаунта!")

@bot.message_handler(commands=['removehabit'])
def handle_removehabit(message):
    user_id = add_or_get_user(message.from_user.id)
    habit_name = "Здоровое питание"  # Здесь можно динамически запросить название привычки от пользователя для удаления
    remove_habit_from_user(user_id, habit_name)
    bot.reply_to(message, f"Привычка '{habit_name}' удалена из вашего аккаунта.")

@bot.message_handler(commands=['listhabits'])
def handle_listhabits(message):
    user_id = add_or_get_user(message.from_user.id)  # Удостоверьтесь, что пользователь зарегистрирован и получите его ID
    habits = list_user_habits(user_id)  # Получение списка привычек пользователя
    if habits:
        habits_text = "\n".join(habits)  # Формирование строки для вывода
        bot.reply_to(message, "Ваши привычки:\n" + habits_text)
    else:
        bot.reply_to(message, "У вас пока нет добавленных привычек.")


bot.polling()
