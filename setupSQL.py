import sqlite2

data = sqlite3.connect("data.db")
cursor = data.cursor()

cursor.execute('''
CREATE TABLE user (
user_id INTAGER PRIMARY KEY,
name INTAGER,
badge INTAGER,
warn INTAGER,
release DATE,

)
''')