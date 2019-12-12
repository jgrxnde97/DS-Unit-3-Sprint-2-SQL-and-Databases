import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# how many total characters are there?
Q1 = 'SELECT COUNT (*) FROM charactercreator_character'
print('number of characters:', curs.execute(Q1).fetchone())

# how many of each specific subclass?
Q2 = 'SELECT COUNT (*) FROM charactercreator_fighter'
print('number of fighters:', curs.execute(Q2).fetchone())

Q2B = 'SELECT COUNT (*) FROM charactercreator_cleric'
print('number of clerics:', curs.execute(Q2B).fetchone())

Q2C = 'SELECT COUNT (*) FROM charactercreator_mage'
print('number of mages:', curs.execute(Q2C).fetchone())

Q2D = 'SELECT COUNT (*) FROM charactercreator_thief'
print('number of thiefs:', curs.execute(Q2D).fetchone())

# how many total items?
Q3 = 'SELECT COUNT (*) FROM armory_item'
print('number of items:', curs.execute(Q3).fetchone())

# how many of the items are weapons?
Q4 = 'SELECT COUNT (*) FROM armory_weapon'
print('number of items that are weapons:', curs.execute(Q4).fetchone())

# how many items does each character have?
# (first 20 rows):
Q5 = """
SELECT COUNT (cci.item_id)
FROM charactercreator_character as cc,
charactercreator_character_inventory as cci
WHERE cci.character_id = cc.character_id
GROUP BY cc.character_id;
"""
print('number of items per character:', curs.execute(Q5).fetchmany(20))

# how many weapons does each characer have?
# (first 20 rows):
Q6 = """
SELECT COUNT (aw.item_ptr_id)
FROM charactercreator_character_inventory as cci,
charactercreator_character as cc,
armory_item as ai,
armory_weapon as aw
WHERE cci.character_id = cc.character_id
AND cci.item_id = ai.item_id,
AND ai.item_id = aw.item_ptr_id
GROUP BY cc.character_id;
"""
print('number of weapons per character:', curs.execute(Q6).fetchmany(20))

# on average, how mnay items does each character have?
Q7 = """
SELECT AVG (avg_items)
FROM (SELECT COUNT (cci.item_id) as avg_items
FROM charactercreator_character as cc,
charactercreator_character_inventory as cci
WHERE cci.character_id = cc.character_id
GROUP BY cc.character_id) AS T;
"""
print('avg num of items per character:', curs.execute(Q7)fetchone())

# on average, how many weapons does each chracter have?
Q8 = """
SELECT AVG (avg_weaps)
FROM (SELECT COUNT(aw.items_ptr_id) as avg_weaps
FROM charactercreator_character_inventory as cci,
charactercreator_characer as cc,
armory_item as ai,
armory_weapon as aw
WHERE cci.character_id = cc.character_id
AND cci.item_id = ai.item_id
AND ai.item_id = aw.item_ptr_id
GROUP BY cc.character_id) AS Z;
"""
print('avg num weapons per character:', curs.execute(Q8).fetchone())

curs.close()
