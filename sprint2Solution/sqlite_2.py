import sqlite3
import psycopg2
import queries as q

dbname='geexrhbt'
user='geexrhbt'
password='Df1qhxwdYreMNa5RnbhO8xPUht0koaie'
host = 'ziggy.db.elephantsql.com'

# Make connection

sqlite_db = "rpg_db.sqlite3"


def lite_connect(sqlite_db):
	sqlite_conn = sqlite3.connect(sqlite_db)
	return sqlite_conn

def create_cursor(conn):
	cursor = conn.cursor()
	return cursor

def execute_query(curs, query, read=True):
	curs.execute(query)
	if read:
		results = curs.fetchall()
		return results
	return 0


if __name__=="__main__":
	pg_conn = psycopg2.connect(dbname=dbname,  user=user,  
						   password=password, host=host)
	
	sl_conn = lite_connect(sqlite_db)
	sl_curs = create_cursor(sl_conn)

	pg_curs = create_cursor(pg_conn)
	results = execute_query(pg_curs, q.create_table_statement, read=False)
	results2 = execute_query(pg_curs, q.test_insert_statement, read=False)
	pg_conn.commit()
	table_name = 'test_table'

	all_data = execute_query(pg_curs, q.select_all.format(table_name))
	all_sqlite_data = execute_query(sl_curs, q.select_all.format('charactercreator_character'))
	print(all_sqlite_data)
	table_info = "PRAGMA table_info(charactercreator_character);"
	table_information = execute_query(sl_curs, table_info)
	print(table_information)



# Making our queries



