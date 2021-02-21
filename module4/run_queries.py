import pymongo
from os import getenv
import pprint


#################################
# RAN SOME OF THE MONGO QUERIES #
#################################

DBASE = 'game_characters'
PASSWORD = getenv('MONGO_DB_PASSWORD')


def mongo_client(db, pswd):
		client = pymongo.\
				MongoClient("mongodb+srv://afro001:{}@cluster0.6jln4.mongodb.net/{}?retryWrites\
							=true&w=majority".format(pswd, db))
		return client




if __name__=="__main__":
	client = mongo_client(DBASE, PASSWORD)
	db = client[DBASE]
	collections = db.posts
	first_item = collections.find_one({'character_id': 1})
	total_characters = len(list(collections.find()))
	
	print("Total Characters: {}".format(total_characters))

	all_items = collections.find({'items':{'$exists': True}})
	items_list = list(all_items)
	print(type(items_list[0]))
	items_count = 0
	for items in items_list:
		items_count += len(items['items'])

	print("Total Items held by all characters is: {}".format(items_count))

	projections = collections.find({},{'weapons':1})
	#print(list(projections))
	weapons_count = 0
	for items in projections:
		weapons_count += len(items['weapons'])

	print("Total Weapons held by all characters is: {}".format(weapons_count))

	print("Average Weapons: {}".format(weapons_count/total_characters))

	print("Average Items: {}".format(items_count/total_characters))

	# In order to return first 20 rows with MongoDB, Read data for each character till 20 Documents are collected
	# Separate and pick only character_id and items_lists, convert items_lists to counts, re-enter data as different post in MongoDB
	# each post should contain character_id and items_count

	first_20_items = collections.find({'character_id': {'$lte':20}},{'character_id':1, 'items': 1})
	#pprint.pprint(list(first_20_items))
	char_items_count = db.char_items
	post = []
	for items in first_20_items:
		posts = {
				'character_id': items['character_id'],
				'count_of_items': len(items['items'])
				}
		post.append(posts)
	
	pprint.pprint(post)
	char_items_count.insert_many(post)









