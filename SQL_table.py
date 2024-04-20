import sqlite3


def setup_database():
    conn = sqlite3.connect('habit_tracker.db')
    cursor = conn.cursor()

    # Включение поддержки внешних ключей
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Создание таблицы пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL
    );
    ''')

    # Создание таблицы привычек с уникальным составным индексом для user_id и habit_name
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        habit_name TEXT NOT NULL,
        habit_description TEXT,
        habit_goal TEXT,
        habit_frequency TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        UNIQUE(user_id, habit_name)
    );
    ''')

    # Создание таблицы пользовательских привычек, которая связывает привычки с пользователями
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_habits (
        user_id INTEGER,
        habit_id INTEGER,
        reminder_frequency TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (habit_id) REFERENCES habits(id) ON DELETE CASCADE
    );
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")


if __name__ == "__main__":
    setup_database()
