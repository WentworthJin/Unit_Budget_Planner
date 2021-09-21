import unittest
import Insert_All_Liangbo_Version
import Create_Table
import getFunction
import sqlite3
import sys
import os
from sqlite3 import Error

'''
   The Test will automatically delete the db file it created 

   *** The test is based on the Insert_All_Liangbo_Version.py, just for convenience ***
   *** However, the functions inside this file is exactly same as the Insert_All.py ***

'''

Create_Table.Schema()
conn = sqlite3.connect("Unit_Budget.db")

class TestCreate(unittest.TestCase):

  # Test if insert_unit function works.
  # The function returns the ID for the unit inserted
  def test_insert_unit(self):
    sample_unit = ["CITS2021","SEN-2",2020]
    result = Insert_All_Liangbo_Version.insert_unit(conn,sample_unit)
    self.assertEqual(result,1)

  # Test if insert_teachingcode function works.
  # The function returns the ID for the TeachingCode inserted.
  def test_insert_teachingcode(self):
    sample_teachingCode = ["TeachingName"]
    result = Insert_All_Liangbo_Version.insert_teachingcode(conn,sample_teachingCode)
    self.assertEqual(result,1)

  # Test if insert_session function works.
  # The function returns the ID for the Session inserted.
  def test_insert_session(self):
    sample_session = ["Lecture","Non-Mark"]
    result = Insert_All_Liangbo_Version.insert_session(conn,sample_session)
    self.assertEqual(result,1)
  
  # Test if insert_nsc function works.
  # The function returns the ID for the non-salary-cost inserted.
  def test_insert_nsc(self):
    sample_nsc = ["Lecture",6,10,60]
    result = Insert_All_Liangbo_Version.insert_nsc(conn,sample_nsc)
    self.assertEqual(result,1)
  
  # Test if insert_enrolment works.
  # The function returns the ID for the Enrolment inserted.
  def test_insert_enrolment(self):
    sample_enrol = [1,200,'Yes','No']
    result = Insert_All_Liangbo_Version.insert_enrolment(conn,sample_enrol)
    self.assertEqual(result,1)
  
  # Test if insert_budget works.
  # The function returns the ID for the Budget inserted.
  def test_insert_budget(self):
    sample_budget = [1,6,"Yes","No"]
    result = Insert_All_Liangbo_Version.insert_budget(conn,sample_budget)
    self.assertEqual(result,1)

  # Test if insert_activities works.
  # The function returns the ID for the Activities inserted.
  def test_insert_activities(self):
    sample_activity = [1,6,3,50,12]
    result = Insert_All_Liangbo_Version.insert_activities(conn,sample_activity)
    self.assertEqual(result,1)

  # Test if insert_othercost works.
  # The function returns the ID for the Othercost inserted.
  def test_insert_oc(self):
    sample_oc = [1,6]
    result = Insert_All_Liangbo_Version.insert_oc(conn,sample_oc)
    self.assertEqual(result,1)
  
  # Test if insert_staff works.
  # The function returns the ID for the Staff inserted.
  def test_insert_staff(self):
    sample_staff = [1,"Racheal","Lecture"]
    result = Insert_All_Liangbo_Version.insert_staff(conn,sample_staff)
    self.assertEqual(result,1)
  

  @classmethod
  def tearDownClass(cls):
    os.remove('Unit_Budget.db')

if __name__ == '__main__':
  unittest.main()