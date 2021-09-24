import unittest
import Insert_All_Liangbo_Version
import Create_Table
import getFunction
import sqlite3
import sys
import os
from sqlite3 import Error

''' 
    *** The Test will automatically delete the database file it created ***

'''
Create_Table.Schema()
conn = sqlite3.connect("Unit_Budget.db")
Insert_All_Liangbo_Version.sample_insert()


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

  @classmethod
  def tearDownClass(cls):
    os.remove('Unit_Budget.db')

if __name__ == '__main__':
  unittest.main()