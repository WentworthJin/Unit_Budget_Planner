import unittest
import Create_Table
import sqlite3
import sys
from sqlite3 import Error

class TestCreate(unittest.TestCase):

  def test_schema(self):
    Create_Table.Schema()
    result = Create_Table.create_connection("Unit_Budget.db") 
    self.assertIsNotNone(result)

if __name__ == '__main__':
  unittest.main()