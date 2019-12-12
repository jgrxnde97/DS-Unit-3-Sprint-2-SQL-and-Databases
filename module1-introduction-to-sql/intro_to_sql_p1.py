import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')
curs = conn.cursor()

# how many total characters are there?
Q1 = 'SELECT COUNT (*) FROM charactercreator_character'
print('number of characters:', curs.execute(Q1).fetchone())

# how many of each specific subclass?
Q2 = 'SELECT COUNT (*) FROM charactercreator_fighter'
print('number of fighters:', curs.exectue(Q2).fetchone())

Q2B = 'SELECT COUNT (*) FROM charactercreator_cleric'
print('number of cleric:', curs.execute(Q2B).fetchone())

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
