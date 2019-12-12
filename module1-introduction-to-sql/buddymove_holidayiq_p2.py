import numpy as np
import pandas as pd
import sqlite3

# read .csv file
df = pd.read_csv('buddymove_holidayiq.csv')

# removing 'space' in column names
df.columns = df.columns.str.replace(' ', '_')

# verify df by checking null vals and shape
print(df.shape)
print(df.isnull().sum())

# creating new database and making connection
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

df.to_sql('review', con=conn)

# how many rows are there?
Q1 = 'SELECT COUNT(*) FROM review':
print('number of rows:', curs.execute(Q1).fetchone())

# how many users who reviewed at least 100 nature in the category also reviewed
# at least 100 in the shopping category?
Q2 = 'SELECT COUNT (*) FROM review WHERE Nature >= 100 and Shopping >= 100';
print('users who reviewed at least 100 in both:', curs.execute(Q2).fetchone())
