import sqlite3

def connect_to_db():
    return sqlite3.connect('habits_tracker.db')

def add_or_get_user(telegram_id):
    conn = connect_to_db()
    cursor = conn.cursor()
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
