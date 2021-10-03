import sqlite3
import sys
import numbers
from sqlite3 import Error

'''
    Functionality: The getFuction.py is also a framework that provides some functions for other users to use, and 
                   enable them to get the primary key of Staff, TeachingCode, and Non-Salary Cost table. 
    
    You can run this file by: Calling the functions inside this file

    Parameters: Certain Table attribute
    
    Result: Return the primary key of the attribute provided

    Testing: Refer to the " test_getID.py " testing file, in order to test if the function can 
             correctly return the primary key of that attribute.

'''

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn

def select_StaffID(conn,Name):

  QueryTemplate = '''Select StaffID From Staff Where Name = {0};'''

  query = QueryTemplate.format(Name)

  cur = conn.cursor()
  cur.execute(query)

  rows = cur.fetchall()

  return rows[0][0]

def select_TeachingCode(conn,TeachingName):

  QueryTemplate = '''Select TeachingCode From TeachingCode Where TeachingName = {0};'''

  query = QueryTemplate.format(TeachingName)

  cur = conn.cursor()
  cur.execute(query)

  rows = cur.fetchall()

  return rows[0][0]

def select_NSCID(conn,NSCName):

  QueryTemplate = '''Select NSCID From NonSalaryCosts Where NSCName = {0};'''

  query = QueryTemplate.format(NSCName)

  cur = conn.cursor()
  cur.execute(query)

  rows = cur.fetchall()

  return rows[0][0]

def main():

  try:
    database = "Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    #Insert Datas
    with conn:

      s = select_StaffID(conn,'''"Racheal"''')
      print(s)

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()

