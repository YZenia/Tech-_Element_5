# Импортируем модуль для работы с SQLite
import sqlite3


# Функция создания базы данных
def setup_database():
    conn = sqlite3.connect('habit_tracker1.db')
    cursor = conn.cursor()

    # Включение поддержки внешних ключей
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Создание таблицы пользователей
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        chat_id TEXT UNIQUE NOT NULL
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
        habit_frequency_per_week INTEGER,
        habit_frequency_per_day INTEGER,
        habit_succesfull INT DEFAULT 0,
        habit_failed INT DEFAULT 0,
        habit_start_date DATE,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
    ''')

    # Создание таблицы прогресса пользователей по привычкам
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_habits (
        user_id INTEGER,
        habit_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY (habit_id) REFERENCES habits (id) ON DELETE CASCADE
    );
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")


# Вызов функции создания базы данных при условии, что файл запущен как основная программа (не import)
if __name__ == "__main__":
    setup_database()
