import unittest
import Insert_All
import Create_Table
import sqlite3
import sys
from sqlite3 import Error

class TestCreate(unittest.TestCase):

  # Test if insert_unit function works.
  def test_insert_unit(self):
    Create_Table.Schema()
    conn = sqlite3.connect("Unit_Budget.db")
    sample_unit = ["CITS2021","SEN-2",2020]
    result = Insert_All.insert_unit(conn,sample_unit)
    self.assertEqual(result,1)


if __name__ == '__main__':
  unittest.main()