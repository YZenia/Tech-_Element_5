# Импортируем модуль для работы с SQLite
import sqlite3


# Подключаемся к базе данных 'habit_tracker1.db'
def connect_to_db():
    return sqlite3.connect('habit_tracker1.db')


# Функция добавления нового пользователя в базу данных или обращения к уже существующему
# Возвращает ID пользователя
def add_or_get_user(username):
    conn = connect_to_db()
    cursor = conn.cursor()

    print(f"DEBUG: Checking if user '{username}' exists in the database.")

    # Проверка, существует ли уже такой пользователь
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]
        print(f"DEBUG: User '{username}' found with ID {user_id}.")
    else:
        print(f"DEBUG: User '{username}' not found, adding to database.")
        # Добавление нового пользователя, если он не найден
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        user_id = cursor.lastrowid
        print(f"DEBUG: New user '{username}' added with ID {user_id}.")

    conn.close()
    return user_id


# Функция добавления новой привычки в базу данных в таблицу 'habits'
# - общая таблица привычек
def add_new_habit(user_id, habit_name, description, goal, frequency):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO habits (user_id, habit_name, habit_description, habit_goal, habit_frequency) "
        "VALUES (?, ?, ?, ?, ?)", (user_id, habit_name, description, goal, frequency)
    )
    conn.commit()
    conn.close()


def add_habit_to_user_list_directly(username, user_id, habit_name, description, goal, frequency='ежедневно'):
    conn = connect_to_db()
    cursor = conn.cursor()
    true_user_id = add_or_get_user(username)
    try:
        # Добавляем привычку в таблицу habits
        cursor.execute("INSERT INTO habits (user_id, habit_name, habit_description, habit_goal, habit_frequency) "
                       "VALUES (?, ?, ?, ?, ?)",
                       (user_id, habit_name, description, goal, frequency))
        habit_id = cursor.lastrowid  # Получаем ID новой привычки
        # Добавляем привычку в список привычек пользователя
        cursor.execute("INSERT INTO user_habits (user_id, habit_id, reminder_frequency) VALUES (?, ?, ?)",
                       (true_user_id, habit_id, frequency))
        conn.commit()
    finally:
        conn.close()


# Функция добавления новой привычки в базу данных в таблицу 'user_habits'
# - привычки конкретного пользователя
def add_habit_to_user_list(user_id, habit_id, frequency='ежедневно'):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user_habits (user_id, habit_id, reminder_frequency) "
        "VALUES (?, ?, ?)", (user_id, habit_id, frequency)
    )
    conn.commit()
    conn.close()


# Функция вывода списка всех привычек из таблицы 'habits'
# def get_all_habits():
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, habit_name FROM habits")
#     habits = cursor.fetchall()
#     conn.close()
#     return habits

# def get_all_habits():
#     """
#     Получить список всех привычек, где user_id равен NULL.
#     Это могут быть общедоступные или стандартные привычки, доступные всем пользователям.
#     """
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     # Изменение запроса для фильтрации привычек, где user_id равен NULL
#     cursor.execute("SELECT id, habit_name FROM habits WHERE user_id IS NULL")
#     habits = cursor.fetchall()
#     conn.close()
#     return habits


# Функция вывода списка всех привычек из таблицы 'habits', кроме тех,
# которые уже в списке пользователя
def get_new_habits(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT h.id, h.habit_name FROM habits h
    WHERE (h.user_id IS NULL) AND (h.id NOT IN (
        SELECT uh.habit_id FROM user_habits uh
        WHERE uh.user_id = ?))
    """, (user_id,)
                   )

    new_habits = cursor.fetchall()
    conn.close()
    return new_habits



# Функция вывода списка всех привычек конкретного пользователя из таблицы 'user_habits'
def get_user_habits(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT uh.user_id, h.habit_name
        FROM user_habits uh
        JOIN habits h ON uh.habit_id = h.id
        WHERE uh.user_id = ?
    """, (user_id,))
    habits = cursor.fetchall()
    conn.close()
    return habits


