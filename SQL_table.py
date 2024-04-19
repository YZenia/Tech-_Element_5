import sqlite3

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