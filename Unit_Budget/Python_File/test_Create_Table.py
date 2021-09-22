import unittest
import Create_Table
import sqlite3
import sys
import os
from sqlite3 import Error


'''
    *** The Test will automatically delete the database file it created ***

'''
os.remove('Unit_Budget.db')

class TestCreate(unittest.TestCase):

  # Check if Shcema & create_connection function works, and wether the 
  # Database has been created. If result is not None, it means the 
  # database has been successfuly created
  def test_schema(self):
    Create_Table.Schema()
    result = Create_Table.create_connection("Unit_Budget.db") 
    self.assertIsNotNone(result)
  
  # Check if create_table fucntion works
  # If result is None, then means this function works properly
  def test_createtable(self):
    conn = Create_Table.create_connection("Unit_Budget.db") 
    result = Create_Table.create_table(conn,'''CREATE TABLE IF NOT EXISTS Test''')
    self.assertIsNone(result)
  
  @classmethod
  def tearDownClass(cls):
    os.remove('Unit_Budget.db')

if __name__ == '__main__':
  unittest.main()