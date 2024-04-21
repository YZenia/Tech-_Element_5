import sqlite3


def setup_database():
    conn = sqlite3.connect('habit_tracker1.db')
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

    # Создание таблицы привычек
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        habit_name TEXT NOT NULL,
        habit_description TEXT,
        habit_goal TEXT,
        habit_frequency TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
    ''')

    # Создание таблицы прогресса пользователей по привычкам
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_habits (
        user_id INTEGER,
        habit_id INTEGER,
        reminder_frequency TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY (habit_id) REFERENCES habits (id) ON DELETE CASCADE
    );
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")



if __name__ == "__main__":
    setup_database()
