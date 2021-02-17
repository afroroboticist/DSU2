import sqlite3
import psycopg2
import queries as q
import re

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


###########################################################
# Prepares query using information from PRAGMA table_info #
###########################################################



def prepare_insert_query(table_information, table_name, data_to_transfer):
	value = "INSERT INTO {} (".format(table_name)
	count=0
	for items in table_information:
		value = value + items[1] 
		count += 1
		if count < len(table_information):
			value = value + ","
	value = value + ") VALUES "
	count2 = 0
	for data in data_to_transfer:
		value = value + "("
		count1 = 0
		for items in data:
			if count1 == 1:
				value = value + "'" + str(items) + "'"
			else:
				value = value + str(items)
			count1 += 1
			if count1 < len(data):
				value += ","
		value = value + ")"
		count2 += 1

		if count2 < len(data_to_transfer):
			value = value + ","
	value = value + ";"
	return value

###############################################
# Data used to test the insert query function #
###############################################

test_data = [(298, 'Autem ratione vitae quos, do', 0, 0, 10, 1, 1, 1, 1), 
			(299, 'Voluptatibus aliquid', 0, 0, 10, 1, 1, 1, 1), 
			(300, 'Quaerat sequi sit eius corpori', 0, 0, 10, 1, 1, 1, 1), 
			(301, 'Libe', 0, 0, 10, 1, 1, 1, 1), 
			(302, 'Aliquam n', 0, 0, 10, 1, 1, 1, 1)]

		

def prepare_table_query(table_name, table_information):
	value = "(id SERIAL PRIMARY KEY, "
	query_statement = "CREATE TABLE IF NOT EXISTS {}".format(table_name)
	count = 0
	for items in table_information:
		value = value +   re.sub(r'[^a-zA-Z0-9]', '', items[1])  + " " + items[2]
		count += 1
		if count < len(table_information):
			value = value + ","
	value = value + ");"

	return query_statement + value

def populate_postgres(sqlite_cursor, sqlite_table, postgres_cursor, postgres_table, table_info):
	data_to_transfer = execute_query(sqlite_cursor, q.select_all.format(sqlite_table))
	query_to_move_data = prepare_insert_query(table_info, postgres_table, data_to_transfer)
	execute_query(postgres_cursor,query_to_move_data, read=False)
	return 0
	#print(data_to_transfer)
	#postgres_cursor.






if __name__=="__main__":
	pg_conn = psycopg2.connect(dbname=dbname,  user=user,  
						   password=password, host=host)
	
	table_of_interest = 'titanic'
	sl_conn = lite_connect(sqlite_db)
	sl_curs = create_cursor(sl_conn)

	pg_curs = create_cursor(pg_conn)
	results = execute_query(pg_curs, q.create_table_statement, read=False)
	results2 = execute_query(pg_curs, q.test_insert_statement, read=False)
	table_name = 'test_table'

	all_data = execute_query(pg_curs, q.select_all.format(table_name))
	all_sqlite_data = execute_query(sl_curs, q.select_all.format('charactercreator_character'))
	#print(all_sqlite_data)
	table_info = "PRAGMA table_info(charactercreator_character);"
	table_information = execute_query(sl_curs, table_info)
	print(table_information)

	statement = prepare_table_query('charactercreator_character', table_information)

	#print(statement)
	new_table = execute_query(pg_curs, statement, read=False)
	

	populate_postgres(sl_curs,table_of_interest, pg_curs, table_of_interest, table_information)
	pg_conn.commit()


	sl_conn.close()

	#data_returned = prepare_insert_query(table_information, table_of_interest, test_data)
	#print(data_returned)





# Making our queries



