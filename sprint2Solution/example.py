import pandas as pd 
import sqlite3
import psycopg2
import queries as q


df = pd.read_csv('https://raw.githubusercontent.com/afroroboticist/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')
print(df.head())