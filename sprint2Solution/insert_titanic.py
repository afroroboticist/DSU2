import pandas as pd 
import sqlite3
import psycopg2
import queries as q
import sqlite_2 as sq
import re


df = pd.read_csv('https://raw.githubusercontent.com/afroroboticist/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
print(df.head())

dbname='geexrhbt'
user='geexrhbt'
password='Df1qhxwdYreMNa5RnbhO8xPUht0koaie'
host = 'ziggy.db.elephantsql.com'


DATABASE = 'titanic.sqlite3'

test_data = [(4, 0, 3, "Mr. William Henry Allen", 'male', 35.0, 0, 0, 8.05), 
			(5, 0, 3, 'Mr. James Moran', 'male', 27.0, 0, 0, 8.4583), 
			(6, 0, 1, 'Mr. Timothy J McCarthy', 'male', 54.0, 0, 0, 51.8625), 
			(7, 0, 3, 'Master. Gosta Leonard Palsson', 'male', 2.0, 3, 1, 21.075), 
			(8, 1, 3, 'Mrs. Oscar W (Elisabeth Vilhelmina Berg) Johnson', 'female', 27.0, 0, 2, 11.1333), 
			(9, 1, 2, 'Mrs. Nicholas (Adele Achem) Nasser', 'female', 14.0, 1, 0, 30.0708)]

###############################################################################
# function prepares a query from individual tuples and from table information #
###############################################################################

def prepare_insert_query(table_information, table_name, data_to_transfer):
	value = "INSERT INTO {} (".format(table_name)
	count=0
	for items in table_information:
		value = value + re.sub(r'[^a-zA-Z0-9]', '', items[1]) 
		count += 1
		if count < len(table_information):
			value = value + ","
	value = value + ") VALUES "
	count2 = 0
	for data in data_to_transfer:
		value = value + "("
		count1 = 0
		for items in data:
			if count1 == 3 or count1 == 4:
				value = value + "'" + str(items).replace("'","") + "'"
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

def execute_query_minimal(curs, query):
	curs.execute(query)
	results = curs.fetchall()
	return results
	
MINIMAL_RETURNED_DATA = 10

if __name__=="__main__":
	pg_conn = psycopg2.connect(dbname=dbname,  user=user,  
						   password=password, host=host)
	
	table_of_interest = 'titanic'

	df = pd.read_csv('https://raw.githubusercontent.com/afroroboticist/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')


	sl_conn = sq.lite_connect(DATABASE)
	sl_curs = sq.create_cursor(sl_conn)

	try:
		df.to_sql(table_of_interest, sl_conn, if_exists='fail')

	except ValueError:
		print('Table already Exists: ',ValueError)

	data = sq.execute_query(sl_curs,q.select_minimal.format(table_of_interest, MINIMAL_RETURNED_DATA))
	print(data)
	

	pg_curs = sq.create_cursor(pg_conn)
	results = sq.execute_query(pg_curs, q.create_table_statement, read=False)

	table_info_query = "PRAGMA table_info(titanic)"
	table_information = sq.execute_query(sl_curs, table_info_query)
	table_prep_query = sq.prepare_table_query(table_of_interest, table_information)
	#print(table_prep_query)
	sq.execute_query(pg_curs, table_prep_query, read=False)

	titanic_data = sq.execute_query(sl_curs, q.select_all.format(table_of_interest))

	insert_query = prepare_insert_query(table_information, table_of_interest, titanic_data)

	new_table = sq.execute_query(pg_curs, insert_query, read=False)



	sl_conn.commit()
	pg_conn.commit()
	sl_conn.close()
	
	# results2 = execute_query(pg_curs, q.test_insert_statement, read=False)
	# table_name = 'test_table'

	# all_data = execute_query(pg_curs, q.select_all.format(table_name))
	# all_sqlite_data = execute_query(sl_curs, q.select_all.format('charactercreator_character'))
	# #print(all_sqlite_data)
	# table_info = "PRAGMA table_info(charactercreator_character);"
	# table_information = execute_query(sl_curs, table_info)
	# print(table_information)

	# statement = prepare_table_query('charactercreator_character', table_information)

	# #print(statement)
	# new_table = execute_query(pg_curs, statement, read=False)
	

	# populate_postgres(sl_curs,table_of_interest, pg_curs, table_of_interest, table_information)
	# pg_conn.commit()


	# sl_conn.close()
