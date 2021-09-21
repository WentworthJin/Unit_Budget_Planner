import unittest
import Insert_All_Liangbo_Version
import Create_Table
import getFunction
import sqlite3
import sys
from sqlite3 import Error

''' Before run this test, it's better to delete the existing db file. However, if you want to 
    run this test stright away, the test can still work.
'''

Create_Table.Schema()
conn = sqlite3.connect("Unit_Budget.db")
Insert_All_Liangbo_Version.main()


class TestCreate(unittest.TestCase):

  # Test if StaffID can be selected
  # The function Returens the StaffID based on the Staff name provided
  def test_get_staffid(self):
    sample_staff = '''"Racheal"'''
    result = getFunction.select_StaffID(conn,sample_staff)
    self.assertEqual(result,1)

  # Test if TeachingCode can be selected
  # The function Returens the TeachingCode based on the Teaching Type provided
  def test_get_tccode(self):
    sample_tcname = '''"TeachingName"'''
    result = getFunction.select_TeachingCode(conn,sample_tcname)
    self.assertEqual(result,1)
  
  # Test if Non-salary-cost ID can be selected
  # The function Returens the Non-salary-cost ID based on the Non-salary-cost Name provided
  def test_get_nscid(self):
    sample_nscname = '''"Lecture"'''
    result = getFunction.select_NSCID(conn,sample_nscname)
    self.assertEqual(result,1)


if __name__ == '__main__':
  unittest.main()