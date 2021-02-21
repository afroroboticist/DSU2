import pymongo
from os import getenv
import sqlite3
import queries as q
import re
import pprint

PASSWORD = getenv('MONGO_PASSWORD')
DBNAME = 'game_characters'



SQLITE_DB = "rpg_db.sqlite3"

character_table = 'charactercreator_character'
weapons_table = 'armory_weapon'
items_table = ''

# Create SQLite3 connection #

def sl_connection(db_name):
	sl_conn = sqlite3.connect(db_name)
	sl_curs = sl_conn.cursor()
	return sl_conn, sl_curs

# Run SQL queries #

def execute_query(curs, query):
	return curs.execute(query).fetchall()

# Create MongoDB Client

def mongo_client(password, dbname):
	client = pymongo.MongoClient(
		"mongodb+srv://afro-001:{}@cluster0.6jln4.mongodb.net/{}?retryWrites=true&w=majority"
		.format(PASSWORD, DBNAME))
	return client


def get_posts(db):
	return db.posts

def show_all(collection):
	all_docs = list(collection.find())
	return all_docs

######################################################
# Populate mongo document with items from MEGA TABLE #
######################################################

def populate_document(posts, mega_table_data, weapons_indexes):
	"""
		mongo_document = {
		  "name": <VALUE>,
		  "level": <VALUE>,
		  "exp": <VALUE>,
		  "hp": <VALUE>,
		  "strength": <VALUE>,
		  "intelligence": <VALUE>,
		  "dexterity": <VALUE>,
		  "wisdom": <VALUE>,
		  "items": [
		    <ITEM NAME>,
		    <ITEM NAME>
		  ],
		  "weapons" [
		    <ITEM NAME>,
		    <ITEM NAME>
		  ]
		}"""
	character_id_track = []

	post = {}
	for item in mega_table_data:
		
		if item[0] not in character_id_track:
			if bool(post) == True:
				post['weapons'] = weapons_list
				post['items'] = items_list
				posts.insert_one(post)
				post = {}
			weapons_list = []
			items_list = []
			character_id_track.append(item[0])

			post = {"character_id": item[0],
					"name": item[1],
					"level": item[2],
					"experience": item[3],
					"hp": item[4],
					"strength": item[5],
					"intelligence": item[6],
					"dexterity": item[7],
					"wisdom": item[8]}
		
			if item[11] in weapons_indexes:
				weapons_list.append(item[12])

			else:
				items_list.append(item[12])

		elif post["character_id"] == item[0]:
		
			if item[11] in weapons_indexes:
				weapons_list.append(item[12])

			else:
				items_list.append(item[12])




	pass

#############################################################################
# Returns a list of ids of items that are weapons. To be used comparatively #
#############################################################################

TEST_DATA = [(281, 'Similique aperiam earum expli', 0, 0, 10, 1, 1, 1, 1, 830, 281, 174, 'Atque repudiandae molestiae v', 174), 
(282, 'Iure h', 0, 0, 10, 1, 1, 1, 1, 831, 282, 16, 'Assu', 16), 
(282, 'Iure h', 0, 0, 10, 1, 1, 1, 1, 832, 282, 161, 'Doloremq', 161), 
(282, 'Iure h', 0, 0, 10, 1, 1, 1, 1, 833, 282, 131, 'Neq', 131), 
(282, 'Iure h', 0, 0, 10, 1, 1, 1, 1, 834, 282, 77, 'Corporis obcaecati ven', 77), 
(283, 'At sint ducimus nostrum i', 0, 0, 10, 1, 1, 1, 1, 835, 283, 96, 'Commodi deserunt in illo', 96), 
(283, 'At sint ducimus nostrum i', 0, 0, 10, 1, 1, 1, 1, 836, 283, 29, 'In p', 29), 
(283, 'At sint ducimus nostrum i', 0, 0, 10, 1, 1, 1, 1, 837, 283, 165, 'Nemo expl', 165), 
(283, 'At sint ducimus nostrum i', 0, 0, 10, 1, 1, 1, 1, 838, 283, 106, 'Et ducimus cumque aut perspic', 106)]

def prune_weapons_list(data):
	weapon_ids = []
	for items in data:
		weapon_ids.append(items[0])
	return weapon_ids


if __name__=="__main__":
	
	# Initiate Mongo Client #
	client = mongo_client(PASSWORD, DBNAME)

	# Initiate Mongo DB #
	db = client[DBNAME]
	posts = db.posts
	#print(db)

	# Create SQLite3 connection and cursor to rpg_db.sqlite3 Database #
	sl_conn, sl_curs = sl_connection(SQLITE_DB)

	# Test Query #
	minimal_query = execute_query(sl_curs, q.select_minimal.format(character_table,10))
	
	# Extract Joined SQL table containing charactercreator_character, character_inventory, and armory_item tables
	mega_table_data = execute_query(sl_curs, q.read_mega_table)
	
	# Extract armory weapons table data to use for separating items from weapons
	amory_weapons_table_data = execute_query(sl_curs, q.select_all.format(weapons_table))
	print(amory_weapons_table_data)

	# Create list of armory_weapon indexes
	weapon_indexes = prune_weapons_list(amory_weapons_table_data)
	print(weapon_indexes)

	# Write all objects into MongoDB document #
	populate_document(posts, mega_table_data, weapon_indexes)

	# Close SQLite3 connection
	sl_conn.close()



