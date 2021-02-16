""" 	queries for slite to postgres pipeline """
select_all = """
	SELECT * FROM {};
	"""


create_table_statement = """
	CREATE TABLE IF NOT EXISTS test_table (
		id SERIAL PRIMARY KEY,
		name varchar(20),
		age INT
	);
	"""


test_insert_statement = """
	INSERT INTO test_table (name, age)
	VALUES ('Steven',25),('Tom',32);
	"""