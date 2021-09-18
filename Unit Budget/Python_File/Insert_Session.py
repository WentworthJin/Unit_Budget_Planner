import sqlite3
import sys
import pandas as pd
from sqlite3 import Error

#create a database connection to a SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

#Insert data into Unit table
def insert_session(conn, session):
    sql = ''' Insert into Session(SessionName,SessionType)
              VALUES(?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, session)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, session)
      conn.commit()
      return cur.lastrowid


def main():

  try:
    database = "Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    #Insert Data
    with conn:

      session = ["Lecture","Non-Mark"]

      insert_session(conn,session)

    print("Dummy Unit data has been inserted")

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()
