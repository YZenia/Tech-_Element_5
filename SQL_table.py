import sqlite3
import telebot
from datetime import datetime
bot = telebot.TeleBot('TOKEN')

# Функция для создания базы данных
def create_database():
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()

    # Создание таблицы привычек
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            habit_name TEXT,
            habit_description TEXT,
            habit_goal TEXT,
            habit_frequency TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    # Создание таблицы выполнения привычек
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS habit_progress (
            id INTEGER PRIMARY KEY,
            habit_id INTEGER,
            progress_date DATE,
            FOREIGN KEY(habit_id) REFERENCES habits(id)
        )
    ''')

    # Создание таблицы пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Функция для добавления привычки с детализацией описания и цели
def add_habit(user_id, habit_name, habit_description, habit_goal, habit_frequency):
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO habits (user_id, habit_name, habit_description, habit_goal, habit_frequency)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, habit_name, habit_description, habit_goal, habit_frequency))

    conn.commit()
    conn.close()

# Функция для получения списка привычек пользователя
def get_user_habits(user_id):
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT habit_name FROM habits WHERE user_id = ?
    ''', (user_id,))

    habits = cursor.fetchall()

    conn.close()

    return habits

# Функция для отправки ежедневного напоминания о привычках
def send_daily_reminder():
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id, user_id FROM users
    ''')
    users = cursor.fetchall()

    for user in users:
        user_id = user[1]
        habits = get_user_habits(user_id)

        if habits:
            habits_list = "\n".join([habit[0] for habit in habits])
            message = f"Привет! Не забудьте сегодня выполнить следующие привычки:\n{habits_list}"
            bot.send_message(user_id, message)

    conn.close()

# Функция для добавления записи о выполнении привычки
def add_progress(user_id, habit_name):
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()

    # Получаем ID привычки
    cursor.execute('''
        SELECT id FROM habits WHERE user_id = ? AND habit_name = ?
    ''', (user_id, habit_name))
    habit_id = cursor.fetchone()

    if habit_id:
        habit_id = habit_id[0]
        progress_date = datetime.now().strftime('%Y-%m-%d')

        cursor.execute('''
            INSERT INTO habit_progress (habit_id, progress_date)
            VALUES (?, ?)
        ''', (habit_id, progress_date))

        conn.commit()
    else:
        print("Привычка не найдена")

    conn.close()

# Пример использования функции для добавления записи о выполнении привычки
#add_progress(3, 'Постоянное обучение')

# Пример использования функции для отправки ежедневного напоминания
#send_daily_reminder()
# Вызов функции для создания базы данных
create_database()

# Пример использования функции для добавления привычки
#add_habit(1, 'Ходьба', 'Питаться ', 'Похудение', 'Ежедневно')