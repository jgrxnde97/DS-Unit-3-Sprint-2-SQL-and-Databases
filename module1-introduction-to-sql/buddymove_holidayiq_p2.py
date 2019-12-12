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
