import sqlite3
from sqlite3 import Error
import queries as q
import pprint


DBNAME = 'Northwind_small.sqlite'


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

table_names = run_query(cursor, q.select_table_names)

print('Names of Tables: ', table_names)

ten_most_expensive = run_query(cursor, q.ten_most_expensive)

print('Ten most Expensive Items: ')
pprint.pprint(ten_most_expensive)

average_age = run_query(cursor, q.average_age)

print('Average age: ', average_age)

average_age_by_city = run_query(cursor, q.average_age_by_city)

print('Average Age By City:')
pprint.pprint(average_age_by_city)

ten_most_expensive_suppliers = run_query(cursor,
                                         q.ten_most_expensive_suppliers)
print('Ten Most Expensive Items with their Suppliers:')
pprint.pprint(ten_most_expensive_suppliers)

largest_category = run_query(cursor, q.largest_category)

print('Largest Category: ', largest_category)

"""
PART 2 -

Ten most Expensive Items:
[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0),
 (29,'Thüringer Rostbratwurst',12,6,'50 bags x 30 sausgs.',123.79,0,0,0,1),
 (9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1),
 (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0),
 (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0),
 (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0),
 (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0),
 (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0),
 (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0),
 (28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]


Average age:  [(37.22222222222222,)]

Average age By City:
[('Kirkland', 29.0),
 ('London', 32.5),
 ('Redmond', 56.0),
 ('Seattle', 40.0),
 ('Tacoma', 40.0)]



PART - 3:

Ten Most Expensive Items with their Suppliers:
[('Côte de Blaye', 'Aux joyeux ecclésiastiques'),
 ('Thüringer Rostbratwurst', 'Plutzer Lebensmittelgroßmärkte AG'),
 ('Mishi Kobe Niku', 'Tokyo Traders'),
 ("Sir Rodney's Marmalade", 'Specialty Biscuits, Ltd.'),
 ('Carnarvon Tigers', 'Pavlova, Ltd.'),
 ('Raclette Courdavault', 'Gai pâturage'),
 ('Manjimup Dried Apples', "G'day, Mate"),
 ('Tarte au sucre', "Forêts d'érables"),
 ('Ipoh Coffee', 'Leka Trading'),
 ('Rössle Sauerkraut', 'Plutzer Lebensmittelgroßmärkte AG')]


Largest Category:  [(13, 'Confections')]

Employee with the most Territories:  [(7, 'Robert', 10)]
    most_territories = run_query(cursor, q.most_territories)

    print('Employee with the most Territories: ',most_territories)
"""
