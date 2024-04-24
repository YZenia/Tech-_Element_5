import sqlite3


conn = sqlite3.connect('habit_tracker1.db')
cursor = conn.cursor()

cursor.execute('''
SELECT user_id, habit_name FROM habits WHERE id = 45
''')

info = cursor.fetchall()

print(info)

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
