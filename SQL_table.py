import sqlite3

<<<<<<< Updated upstream
def setup_database():
    # Создаем подключение к базе данных SQLite
    with sqlite3.connect('habits_tracker.db') as conn:
        cursor = conn.cursor()

        # Создаем таблицу пользователей
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')

        # Создаем таблицу привычек
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS habits (
            habit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            type TEXT CHECK(type IN ('custom', 'preset')) DEFAULT 'preset',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')

        # Создаем таблицу связей пользователей с привычками
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_habits (
            user_id INTEGER,
            habit_id INTEGER,
            reminder_frequency TEXT CHECK(reminder_frequency IN ('daily', 'weekly', 'monthly')) NOT NULL,
            PRIMARY KEY (user_id, habit_id),
            FOREIGN KEY (user_id) REFERENCES users(user_id),
            FOREIGN KEY (habit_id) REFERENCES habits(habit_id)
        );
        ''')

        # Наполняем таблицу привычек начальными данными
        habits = [("Табакокурение", "🚬", "bad"), ("Здоровое питание", "🥗", "good")]
        cursor.executemany("INSERT INTO habits (name, description, type) VALUES (?, ?, ?)", habits)

        # Сохраняем изменения
        conn.commit()

if __name__ == "__main__":
    setup_database()
=======
def connect_to_db():
    return sqlite3.connect('habits_tracker.db')

def add_or_get_user(telegram_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users (telegram_id) VALUES (?)", (telegram_id,))
    conn.commit()
    cursor.execute("SELECT user_id FROM users WHERE telegram_id = ?", (telegram_id,))
    user_id = cursor.fetchone()[0]
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
    cursor.execute("SELECT h.name FROM habits h JOIN user_habits uh ON h.habit_id = uh.habit_id WHERE uh.user_id = ?", (user_id,))
    habits = cursor.fetchall()
    conn.close()
    return [habit[0] for habit in habits]

if __name__ == "__main__":
    # Это место для тестирования функций, если потребуется
    # Пример вызова функции: print(list_user_habits(1))
    pass
>>>>>>> Stashed changes
