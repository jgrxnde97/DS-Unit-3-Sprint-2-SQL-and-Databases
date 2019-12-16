# part one: making and populating a database
import sqlite3

# making sqlite connection and cursor
conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

# creating table
# variable t = table
def demo_create():
    t = '''CREATE TABLE demo(
        s text NOT NULL,
        x integer NOT NULL,
        y integer NOT NULL
    )'''
    curs.execute(t)

demo_create()

# inserting data into table
def demo_insert():
    t1 = """INSERT INTO demo VALUES
    ('g', 3, 9)
    ('v', 5, 7)
    ('f', 8, 7)"""
    curs.execute(t1)

demo_insert()

# save
def demo_save():
    conn.commit()

demo_save()

# count num rows
def row_count():
    a = """
    SELECT COUNT (s)
    FROM demo
    """
    curs.execute(a)
    return curs.fetchall()

row_count()

# how many rows where 'x' and 'y' are at least 5?
def min_count():
    a2 = """
    SELECT COUNT (*)
    FROM demo
    WHERE x >= 5 and y >=5
    """
    curs.execute(a2)
    return curs.fetchall()

min_count()

# how many unique values of 'y' are there?
def uni_count():
    a3 = """
    SELECT COUNT(DISTINCT y)
    FROM demo
    """
    curs.execute(a3)
    return curs.fetchall()

uni_count()
