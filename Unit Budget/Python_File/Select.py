import sqlite3
import sys
import pandas as pd
from sqlite3 import Error

query = '''Select UnitID From Unit Where UnitCode = "CITS2021" '''

#create a database connection to a SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def select_all_tasks(conn):

    cur = conn.cursor()
    cur.execute(query)

    rows = cur.fetchall()

    print(rows[0][0])


def main():

  try:
    database = "Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    #Insert Data
    with conn:

      select_all_tasks(conn)

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()

