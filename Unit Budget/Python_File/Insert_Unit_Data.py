import sqlite3
import sys
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
def create_unit(conn, unit):
    sql = ''' INSERT INTO Unit(UnitID,UnitCode,Semester,Year)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, unit)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, unit)
      conn.commit()
      return cur.lastrowid


def main():

  try:
    database = "./DataBase/Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    #Insert Data
    with conn:
      Unit1 = ('1','CITS5503','2','2020')
      Unit2 = ('2','CITS4401','1','2020')
      Unit3 = ('3','CITS1101','1','2021')

      create_unit(conn,Unit1)
      create_unit(conn,Unit2)
      create_unit(conn,Unit3)

    print("Dummy Unit data has been inserted")

  except Error:
    print("Some of the data has already been entered, please check again")

if __name__ == '__main__':
  main()

