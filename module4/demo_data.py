import sqlite3
from sqlite3 import Error
import queries as q


DBNAME = 'demo_data.sqlite3'

data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]


def make_connection(dbname):
    """Create a database and return its cursor along with its connection"""
    conn = None
    cursor = None

    try:
        conn = sqlite3.connect(dbname)
    except Error as e:
        print('Error encountered while creatind Dbase: {}'.format(e))

    if conn:
        cursor = conn.cursor()

    return conn, cursor


def run_query(cursor, query, read=True):
    cursor.execute(query)
    if read:
        return cursor.fetchall()

    return None


conn, cursor = make_connection(DBNAME)
print(conn, cursor)

table_name = 'demo'
run_query(cursor, q.create_table.format(table_name), read=False)

for items in data:
    run_query(cursor, q.insert_data.format(table_name, items[0],
                                           items[1], items[2]), read=False)

conn.commit()

row_count = run_query(cursor, q.row_count.format(table_name))

print(row_count)

xy_at_least_5 = run_query(cursor, q.xy_at_least_5.format(table_name))

print(xy_at_least_5)

unique_y = run_query(cursor, q.unique_y.format(table_name))

print(unique_y)
