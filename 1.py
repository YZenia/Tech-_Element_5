import sqlite3

def connect_to_db():
    # Замените 'your_database.db' на путь к вашей базе данных
    return sqlite3.connect('habit_tracker1.db')

def get_user_habits(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    # Обновленный SQL-запрос
    cursor.execute("""
        SELECT h.habit_name
        FROM user_habits uh
        JOIN habits h ON uh.habit_id = h.id
        WHERE uh.user_id = ?
    """, (user_id,))
    habits = cursor.fetchall()
    conn.close()
    return habits

# Замените '1' на актуальный ID пользователя, для которого вы хотите получить данные
user_id = 1
habits = get_user_habits(user_id)
print(f"Habits for user {user_id}: {habits}")
