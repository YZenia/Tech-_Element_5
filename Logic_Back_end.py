import sqlite3

def connect_to_db():
    return sqlite3.connect('habits_tracker.db')

def add_or_get_user(telegram_id):
    conn = connect_to_db()
    cursor = conn.cursor()
<<<<<<< Updated upstream
    cursor.execute("INSERT OR IGNORE INTO users (telegram_id) VALUES (?)", (telegram_id,))
    conn.commit()
    cursor.execute("SELECT user_id FROM users WHERE telegram_id=?", (telegram_id,))
    user_id = cursor.fetchone()[0]
    conn.close()
    return user_id

def add_custom_habit(user_id, habit_name, description, frequency):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO habits (name, description, type) VALUES (?, ?, 'custom')", (habit_name, description))
    habit_id = cursor.lastrowid
    cursor.execute("INSERT INTO user_habits (user_id, habit_id, reminder_frequency) VALUES (?, ?, ?)", (user_id, habit_id, frequency))
    conn.commit()
    conn.close()

def remove_user_habit(user_id, habit_name):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user_habits WHERE user_id=? AND habit_id=(SELECT habit_id FROM habits WHERE name=?)", (user_id, habit_name))
    conn.commit()
    conn.close()

def list_habits():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM habits")
    habits = cursor.fetchall()
    conn.close()
    return [habit[0] for habit in habits]

def habit_exists(user_id, habit_name):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT EXISTS(SELECT 1 FROM user_habits WHERE user_id=? AND habit_id=(SELECT habit_id FROM habits WHERE name=?))", (user_id, habit_name))
    exists = cursor.fetchone()[0]
    conn.close()
    return bool(exists)
=======
    # Проверяем, существует ли пользователь с таким telegram_id
    cursor.execute("SELECT user_id FROM users WHERE telegram_id = ?", (telegram_id,))
    user = cursor.fetchone()
    if user:
        # Если пользователь существует, возвращаем его user_id
        user_id = user[0]
    else:
        # Если пользователя нет, добавляем его в базу данных и получаем новый user_id
        cursor.execute("INSERT INTO users (telegram_id) VALUES (?)", (telegram_id,))
        conn.commit()
        user_id = cursor.lastrowid  # Получаем user_id только что добавленного пользователя
    conn.close()
    return user_id


def add_habit_to_user(user_id, habit_name):
    conn = connect_to_db()
    cursor = conn.cursor()
    # Проверяем, существует ли такая привычка
    cursor.execute("SELECT habit_id FROM habits WHERE name = ?", (habit_name,))
    habit_data = cursor.fetchone()
    if habit_data is not None:
        habit_id = habit_data[0]
        # Добавляем привычку пользователю
        cursor.execute("INSERT OR IGNORE INTO user_habits (user_id, habit_id) VALUES (?, ?)", (user_id, habit_id))
        conn.commit()
    conn.close()

def remove_habit_from_user(user_id, habit_name):
    conn = connect_to_db()
    cursor = conn.cursor()
    # Находим ID привычки по её названию
    cursor.execute("SELECT habit_id FROM habits WHERE name = ?", (habit_name,))
    habit_data = cursor.fetchone()
    if habit_data is not None:
        habit_id = habit_data[0]
        # Удаляем привычку у пользователя
        cursor.execute("DELETE FROM user_habits WHERE user_id = ? AND habit_id = ?", (user_id, habit_id))
        conn.commit()
    conn.close()

def list_user_habits(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT h.name FROM habits h 
        JOIN user_habits uh ON h.habit_id = uh.habit_id 
        WHERE uh.user_id = ?""", (user_id,))
    habits = cursor.fetchall()
    conn.close()
    return [habit[0] for habit in habits]  # Возвращает список названий привычек

if __name__ == "__main__":
    # Это место для тестирования функций, если потребуется
    # Пример вызова функции: print(list_user_habits(1))
    pass
>>>>>>> Stashed changes
