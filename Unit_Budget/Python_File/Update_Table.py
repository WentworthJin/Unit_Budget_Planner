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

#Update Function
def update_unit(conn, unit):

    sql = ''' UPDATE Unit
              SET UnitCode = ? ,
                  Semester = ?,
                  Year = ?
              WHERE UnitID = ?'''
    cur = conn.cursor()
    cur.execute(sql, unit)
    conn.commit()

def main():

  try:
    database = "./DataBase/Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    with conn:
      update_unit(conn,('CITS2203',2,2022,3))
      
  except Error:
    print("No such DB")
    print("Please check your DB name again")


if __name__ == '__main__':
  main()