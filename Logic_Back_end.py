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
    # true_user_id = add_or_get_user(user_id)
    # print(true_user_id)
    # # result = cursor.execute(
    # #     "SELECT id, user_id  FROM users_habits WHERE username = ?", (user_id,)
    # # )
    # # print(result)
    # cursor.execute(
    #     "SELECT SELECT COUNT(habit_id)  FROM user_habits WHERE user_id = ?", (true_user_id,)
    # )
    # count = cursor.fetchone()[0]
    # print(f'Количество {count}')
    # if count >= 3:
    #     return print(f"Maximum number of habits reached.\n"
    #                  f"Cannot add more habits.")
    # else:
    cursor.execute(""
                   "INSERT INTO habits (user_id, habit_name, habit_description, habit_goal, habit_frequency) "
                   "VALUES (?, ?, ?, ?, ?)"
                   "", (user_id, habit_name, description, goal, frequency))
    conn.commit()
    conn.close()


# Функция добавления новой привычки в базу данных - и в таблицу habits, и в таблицу user_habits
def add_habit_to_user_list_directly(username, user_id, habit_name, description, goal, frequency='ежедневно'):
    conn = connect_to_db()
    cursor = conn.cursor()
    true_user_id = add_or_get_user(username)
    print(f"USER_ID {true_user_id}")
    try:
        # Добавляем привычку в таблицу habits
        cursor.execute("INSERT INTO habits (user_id, habit_name, habit_description, habit_goal, habit_frequency) "
                       "VALUES (?, ?, ?, ?, ?)",
                       (true_user_id, habit_name, description, goal, frequency))
        habit_id = cursor.lastrowid  # Получаем ID новой привычки
        # Добавляем привычку в список привычек пользователя
        cursor.execute("INSERT INTO user_habits (user_id, habit_id, reminder_frequency) VALUES (?, ?, ?)",
                       (true_user_id, habit_id, frequency))
        conn.commit()
    finally:
        conn.close()


# Функция добавления новой привычки в таблицу 'user_habits' - привычки конкретного пользователя
def add_habit_to_user_list(user_id, habit_id, frequency='ежедневно'):
    conn = connect_to_db()
    try:
        cursor = conn.cursor()
        add_or_get_user(user_id)

        cursor.execute(
            "SELECT COUNT(habit_id) FROM user_habits WHERE user_id = ?", (user_id,)
        )
        count = cursor.fetchone()[0]

        if count >= 3:  # Ограничение - не более 3х привычек на 1го пользователя
            print("Максимальное количество привычек достигнуто.")
            return None
        else:
            cursor.execute(
                "INSERT INTO user_habits (user_id, habit_id, reminder_frequency) "
                "VALUES (?, ?, ?)", (user_id, habit_id, frequency)
            )
            conn.commit()
            print("Привычка успешно добавлена.")
            return True
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None
    finally:
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
        SELECT uh.user_id, h.habit_name, h.id
        FROM habits h
        JOIN user_habits uh ON h.id = uh.habit_id
        WHERE uh.user_id = ?
    """, (user_id,))
    habits = cursor.fetchall()
    conn.close()
    return habits


# Функция вывода информации о привычке из таблицы 'habits'
def get_habit_info(habit_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT h.habit_name, h.habit_description, h.habit_goal
        FROM habits h
        WHERE h.id = ?
    """, (habit_id,))
    habit_details = cursor.fetchall()
    conn.close()
    return habit_details


# Функция удаления привычки из таблицы 'user_habits'
def delete_habit_by_id(habit_id, user_id):
    try:
        with connect_to_db() as conn:
            cursor = conn.cursor()
            # Удаление привычки из таблицы user_habits
            cursor.execute("DELETE FROM user_habits WHERE (habit_id = ? AND user_id = ?)",
                           (habit_id, user_id, ))
            # Удаление привычки из таблицы habits - ЗАЧЕМ?
            # cursor.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
            conn.commit()
            print("Привычка успешно удалена.")
            return True
    except Exception as e:
        print(f"Ошибка при удалении привычки: {e}")
        return False





