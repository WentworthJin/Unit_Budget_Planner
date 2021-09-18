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
def insert_unit(conn, unit):
    sql = ''' INSERT INTO Unit(UnitCode,Semester,Year)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, unit)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, unit)
      conn.commit()
      return cur.lastrowid


def main():
  pd.set_option("max_columns", 10)
  folder ="CITS1001_Sem1,2021 budget v3.xlsx"
  unit_detail = pd.read_excel(folder,usecols ="A:B",header =8,nrows=5)
  UnitCode =unit_detail.iloc[0,1]
  Semester=unit_detail.iloc[1,1]
  Year =unit_detail.iloc[4,1]

  try:
    database = "Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    #Insert Data
    with conn:
      Unit = (UnitCode,Semester,Year)

      insert_unit(conn,Unit)

    print("Dummy Unit data has been inserted")

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()

