import sqlite3

conn = sqlite3.connect('task1.db')

sql_query = """
CREATE TABLE IF NOT EXISTS Tasks (
  id INTEGER PRIMARY KEY,
  task_name TEXT, 
  date_created datetime default current_timestamp
  
);
"""

conn.execute(sql_query)
conn.close()