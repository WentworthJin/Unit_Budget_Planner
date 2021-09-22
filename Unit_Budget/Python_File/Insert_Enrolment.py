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

#Insert data into Enrolment table
def insert_enrolment(conn, enrol):
    sql = ''' Insert into Enrolment(UnitID,EnrolmentNumber,IsEstimated,IsLastSemester)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, enrol)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, enrol)
      conn.commit()
    else:
      return cur.lastrowid


def main():

  try:
    database = "Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    #Insert Data
    with conn:

      enrol = [1,200,'Yes','No']

      insert_enrolment(conn,enrol)

    print("Dummy Unit data has been inserted")

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()
