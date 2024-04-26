import sqlite3


user_id = 8
conn = sqlite3.connect('habit_tracker1.db')
cursor = conn.cursor()

cursor.execute(
    '''SELECT COUNT(habit_id)  FROM user_habits WHERE user_id = 8'''
)
count = cursor.fetchone()[0]  # Получаем результат запроса (первая строка, первый столбец)
print(f"User {user_id} has {count} habits.")

if count >= 3:
    print(f"Maximum number of habits reached.\n"
          f"Cannot add more habits.")

#print(cursor.fetchall())
# result = []
# for i in cursor:
#     result.append(i[1])
# if len(result) > 10:
#     print(f'Слишком много привычек для контроля и исполнения')
# else:
#     print(result)

# result = cursor.fetchall.rowcount()
# print(result)

# cursor.execute('''
# SELECT user_id, habit_name FROM habits WHERE id = 45
# ''')
#
# info = cursor.fetchall()
#
# print(info)

conn.commit()
conn.close()

# cursor.execute('''
# DELETE FROM habits WHERE id = 52
# ''')
#
# cursor.execute('''
# DELETE FROM user_habits WHERE habit_id = 52
# ''')


# print("Database and tables updated successfully.")
