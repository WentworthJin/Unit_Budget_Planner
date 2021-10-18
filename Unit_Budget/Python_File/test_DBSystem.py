import unittest
import Insert_All_Liangbo_Version
import Create_Table
import getFunction
import sqlite3
import sys
import os
from sqlite3 import Error


'''
    *** The Test will test the overall functionality of the Database ***
    *** Including the Table Creation and Insertion ***

'''

class TestCreate(unittest.TestCase):

  # Check if Shcema & create_connection function works, and wether the 
  # Database has been created. If result is not None, it means the 
  # database has been successfuly created
  def test_schema(self):
    Create_Table.Schema()
    result = Create_Table.create_connection("BudgetSample.db") 
    self.assertIsNotNone(result)
  
  # Check if create_table fucntion works
  # If result is None, then means this function works properly
  def test_createtable(self):
    conn = Create_Table.create_connection("BudgetSample.db") 
    result = Create_Table.create_table(conn,'''CREATE TABLE IF NOT EXISTS Test''')
    self.assertIsNone(result)
  
  # Test Table and single data Inseration
  def test_insert_unit(self):
    Create_Table.Schema()
    conn = sqlite3.connect("BudgetSample.db")

     # Test Unit Table
    sample_unit = ["Computing","CITS2021","SEM-2",2020]
    result_unit = Insert_All_Liangbo_Version.insert_unit(conn,sample_unit)
    # Test TeachingCode Table
    sample_teachingCode = ["TeachingName"]
    result_tc = Insert_All_Liangbo_Version.insert_teachingcode(conn,sample_teachingCode)
    # Test Session Table
    sample_session = ["Lecture","NM"]
    result_session = Insert_All_Liangbo_Version.insert_session(conn,sample_session)
    # Test NonSalaryCost Table
    sample_nsc = ["Lecture",6,10,60]
    result_nsc = Insert_All_Liangbo_Version.insert_nsc(conn,sample_nsc)
    # Test Enrolment Table
    sample_enrol = [1,200,'Yes','No']
    result_enrol = Insert_All_Liangbo_Version.insert_enrolment(conn,sample_enrol)
    # Test Budget Table
    sample_budget = [1,6,"Yes","No"]
    result_budget = Insert_All_Liangbo_Version.insert_budget(conn,sample_budget)
    # Test Activities Table
    sample_activity = [1,1,1,4,0.25,30,60]
    result_act = Insert_All_Liangbo_Version.insert_activities(conn,sample_activity)
    # Test OtherCost Table
    sample_oc = [1,6]
    result_oc = Insert_All_Liangbo_Version.insert_oc(conn,sample_oc)
    # Test Staff Table
    sample_staff = [1,"Racheal","Lecture"]
    result_staff = Insert_All_Liangbo_Version.insert_staff(conn,sample_staff)
    self.assertEqual(result_unit,1)
    self.assertEqual(result_tc,1)
    self.assertEqual(result_session,1)
    self.assertEqual(result_nsc,1)
    self.assertEqual(result_enrol,1)
    self.assertEqual(result_budget,1)
    self.assertEqual(result_act,1)
    self.assertEqual(result_oc,1)
    self.assertEqual(result_staff,1)

  @classmethod
  def tearDownClass(cls):
    os.remove('BudgetSample.db')

if __name__ == '__main__':
  unittest.main()