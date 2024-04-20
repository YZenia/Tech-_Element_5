import sqlite3

def connect_to_db():
    return sqlite3.connect('habit_tracker1.db')

def add_or_get_user(username):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user:
        user_id = user[0]
    else:
        cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
        conn.commit()
        user_id = cursor.lastrowid
    conn.close()
    return user_id

def add_new_habit(user_id, habit_name, description, goal, frequency):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO habits (user_id, habit_name, habit_description, habit_goal, habit_frequency) VALUES (?, ?, ?, ?, ?)", (user_id, habit_name, description, goal, frequency))
    conn.commit()
    conn.close()

def add_habit_to_user_list(user_id, habit_id, frequency='ежедневно'):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_habits (user_id, habit_id, reminder_frequency) VALUES (?, ?, ?)", (user_id, habit_id, frequency))
    conn.commit()
    conn.close()

def get_all_habits():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, habit_name FROM habits")
    habits = cursor.fetchall()
    conn.close()
    return habits
def get_user_habits(user_id):
    conn = connect_to_db()  # Убедитесь, что эта функция правильно подключается к вашей базе данных
    cursor = conn.cursor()
    # Обновленный запрос для извлечения названий привычек пользователя по его ID
    cursor.execute("""
     SELECT h.habit_name
     FROM user_habits uh
     JOIN habits h ON uh.habit_id = h.id
     WHERE uh.user_id = ?

        """, (user_id,))
    habits = cursor.fetchall()  # Получаем все записи, удовлетворяющие запросу
    conn.close()  # Закрываем соединение с базой данных
    return habits  # Возвращаем список привычек пользователя


# def get_user_habits(user_id):
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT uh.user_id, h.habit_name, uh.reminder_frequency FROM user_habits uh JOIN habits h ON uh.habit_id = h.id WHERE uh.user_id = ?", (user_id,))
#     habits = cursor.fetchall()
#     print("DEBUG: Retrieved habits:", habits)  # Добавить для отладки
#     conn.close()
#     return habits

