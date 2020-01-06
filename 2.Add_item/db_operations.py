import sqlite3


def execute_query(sql_query):
    with sqlite3.connect("task.db") as con:
        cur = con.cursor()
        result = cur.execute(sql_query)
        con.commit()
    return result


def add_tasks(task):
    sql_query = """insert into Tasks(task_name) VALUES ( '%s' )""" % (task)
    execute_query(sql_query)


def get_tasks():
    sql_query = """select task_name from Tasks"""
    return execute_query(sql_query).fetchall()