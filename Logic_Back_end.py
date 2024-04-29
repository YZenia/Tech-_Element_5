# Импортируем модуль для работы с SQLite
import sqlite3
import datetime


# Подключаемся к базе данных 'habit_tracker1.db'
def connect_to_db():
    return sqlite3.connect('habit_tracker1.db')


# Функция добавления нового пользователя в базу данных

def add_user(username, chat_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    print(f"DEBUG: Checking if user '{username}' exists in the database.")
    # Проверка, существует ли уже такой пользователь
    cursor.execute("SELECT id FROM users WHERE username = (?)", (username,))
    result = cursor.fetchone()
    if result:
        user_id = result[0]
        print(
            f"DEBUG: User '{username}' found with ID {user_id}. chat_id: {chat_id}")
    else:
        print(f"DEBUG: User '{username}' not found, adding to database.")
        # Добавление нового пользователя, если он не найден
        cursor.execute(
            "INSERT INTO users (username, chat_id) VALUES (?,?)", (username, chat_id))
        conn.commit()
        user_id = cursor.lastrowid
        print(
            f"DEBUG: New user '{username}' added with ID {user_id}.chat_id: {chat_id}")
    conn.close()

# Возвращает ID пользователя по нику


def get_user_id_by_username(username):
    conn = connect_to_db()
    cursor = conn.cursor()

    print(f"DEBUG: Checking if user '{username}' exists in the database.")

    # Проверка, существует ли такой пользователь
    cursor.execute("SELECT id FROM users WHERE username = (?)", (username,))
    result = cursor.fetchone()
    if result:
        user_id = result[0]
        return user_id
    conn.close()
    return 0

# IN FUTURE


def get_user_chat_id_by_username(username):
    conn = connect_to_db()
    cursor = conn.cursor()

    print(f"DEBUG: Checking if user '{username}' exists in the database.")

    # Проверка, существует ли такой пользователь
    cursor.execute(
        "SELECT chat_id FROM users WHERE username = (?)", (username,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]
        return user_id
    conn.close()
    return 0

# Счетчик выполнения


def get_all_user_habits_id(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_habits WHERE user_id= (?)", (user_id,))
    all_user_habits_id = cursor.fetchall()
    return all_user_habits_id


def get_habit_by_id(habit_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM habits WHERE id= (?)", (habit_id,))
    habit = cursor.fetchall()
    return habit


def set_habit_result(habit_id, result):
    conn = connect_to_db()
    cursor = conn.cursor()
    match result:
        case 1:
            cursor.execute(
                "SELECT habit_succesfull FROM habits WHERE id= (?)", (habit_id,))
            success_value = cursor.fetchone()
            success_value = success_value[0] + 1
            try:
                print(f"update value {success_value}")
                print(f"update id{habit_id}")

                cursor.execute(
                    "UPDATE habits SET habit_succesfull= ? WHERE id= ?", (success_value, habit_id))
                conn.commit()

            finally:
                conn.close()
        case 0:
            cursor.execute(
                "SELECT habit_succesfull FROM habits WHERE id= (?)", (habit_id,))
            failed_value = cursor.fetchone()
            failed_value = failed_value[0] + 1
            try:
                cursor.execute(
                    "UPDATE habits SET habit_failed= ? WHERE id= ?", (failed_value, habit_id))
                conn.commit()

            finally:
                conn.close()

# Функция добавления новой привычки в базу данных - и в таблицу habits, и в таблицу user_habits


def add_habit_to_user_list_directly(username, user_id, habit_name, description, goal, frequency_per_week, frequency_per_day):
    conn = connect_to_db()
    cursor = conn.cursor()
    true_user_id = get_user_id_by_username(username)
    habit_start_date_and_time = datetime.datetime.today()
    print(f"USER_ID {true_user_id}")
    try:
        # Добавляем привычку в таблицу habits
        cursor.execute("INSERT INTO habits (user_id, habit_name, habit_description, habit_goal, habit_frequency_per_week, habit_frequency_per_day, habit_start_date)"
                       "VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (true_user_id, habit_name, description, goal, frequency_per_week, frequency_per_day, habit_start_date_and_time))
        habit_id = cursor.lastrowid  # Получаем ID новой привычки
        # Добавляем привычку в список привычек пользователя
        cursor.execute("INSERT INTO user_habits (user_id, habit_id) VALUES (?, ?)",
                       (true_user_id, habit_id))
        conn.commit()
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

def get_all_habits():
    """
    Получить список всех привычек, где user_id равен NULL.
    Это могут быть общедоступные или стандартные привычки, доступные всем пользователям.
    """
    conn = connect_to_db()
    cursor = conn.cursor()
    # Изменение запроса для фильтрации привычек, где user_id равен NULL
    cursor.execute("SELECT id, habit_name FROM habits WHERE user_id IS NULL")
    habits = cursor.fetchall()
    conn.close()
    return habits


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
        SELECT h.habit_name, h.habit_description, h.habit_goal, h.habit_frequency_per_week, habit_frequency_per_day, habit_succesfull, habit_failed, habit_start_date
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
