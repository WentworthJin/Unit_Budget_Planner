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


#Delete based on row id in Unit Table
def delete_task(conn, UnitID):

    sql = 'DELETE FROM Unit WHERE UnitID=?'
    cur = conn.cursor()
    cur.execute(sql, (UnitID,))
    conn.commit()


#Delete all rows in Unit Table
def delete_all_unit(conn):
    sql = 'DELETE FROM Unit'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():

  try:
    database = "./DataBase/Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    #Insert Data
    with conn:
      delete_task(conn,3)

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()