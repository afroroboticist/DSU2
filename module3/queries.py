""" 	queries for slite to postgres pipeline """
select_all = """
	SELECT * FROM {};
	"""

select_minimal = """
	SELECT * FROM {} LIMIT {};
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

read_mega_table = """
	SELECT * FROM (SELECT * FROM charactercreator_character cc join 
	charactercreator_character_inventory ci ON cc.character_id = ci.character_id) combo
	JOIN (SELECT name, item_id from armory_item) ai ON combo.item_id = ai.item_id
	"""