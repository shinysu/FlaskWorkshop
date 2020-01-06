import sqlite3

conn = sqlite3.connect('task.db')

sql_query = """
CREATE TABLE IF NOT EXISTS Tasks (
  id INTEGER PRIMARY KEY,
  task_name TEXT
  
);
"""

conn.execute(sql_query)
conn.close()