import unittest
import Insert_All
import Create_Table
import pandas as pd
import sqlite3
import sys
import os
from sqlite3 import Error

#This test is used to test Insert_All.py

#Which include the function of retrieve data from excel file and import into database

#The Test will automatically delete the database file it created


# create a new database with same table structure.
Create_Table.Schema()
conn = sqlite3.connect("Unit_Budget.db")
pd.set_option("max_columns", 10)
file ="CITS1001_Sem1,2021 budget v3.xlsx"
unit_detail,unit_strcture,resourcing,NSC = Insert_All.get_details(file)



class TestCreate(unittest.TestCase):

  #test if get detail can retrieve data from given excel file
  def test_get_unitcode(self):
      UnitCode =unit_detail.iloc[0,1]
      self.assertEqual(UnitCode,"CITS1001")

  def test_get_unityear(self):
      Year =unit_detail.iloc[4,1]
      self.assertEqual(Year,2021)

  def test_get_NSC(self):
      NSCNames = NSC.iloc[:3,0][0]
      self.assertEqual(NSCNames,"Workshop/technician time")

  def test_get_TeachingCode(self):
      teachingcodes = resourcing.iloc[0:7,3][0]
      self.assertEqual(teachingcodes,"No cost")

  def test_get_sessionName(self):
      sessionNames =unit_strcture.iloc[0:12,0][0]
      self.assertEqual(sessionNames,"Lectures")

      

  # Test if insert_unit function works.
  # The function returns the ID for the unit inserted
  def test_insert_unit(self):
    sample_unit = ["CITS1001","SEM-1",2021]
    result = Insert_All.insert_unit(conn,sample_unit)
    # select all from unit table where unitid is what we just inserted 
    result1 = Insert_All.select_query(conn,'Select * from unit where unitid = '+str(result))
    sample_unit.insert(0,result)
    # the query return a list of tuples, in order to compare, need to convert their data type
    self.assertEqual(result1[0],tuple(sample_unit))

  # Test if insert_teachingcode function works.
  # The function returns the ID for the TeachingCode inserted.
  def test_insert_teachingcode(self):
    sample_teachingCode = ["TeachingName"]
    result = Insert_All.insert_teachingcode(conn,sample_teachingCode)
    result1 = Insert_All.select_query(conn,'Select * from teachingcode where teachingcode = '+str(result))
    sample_teachingCode.insert(0,result)
    self.assertEqual(result1[0],tuple(sample_teachingCode))

  # Test if insert_session function works.
  # The function returns the ID for the Session inserted.
  def test_insert_session(self):
    sample_session = ["Lab","Non-Mark"]
    result = Insert_All.insert_session(conn,sample_session)
    result1 = Insert_All.select_query(conn,'Select * from session where sessionID = '+str(result))
    sample_session.insert(0,result)
    self.assertEqual(result1[0],tuple(sample_session))
  
  # Test if insert_nsc function works.
  # The function returns the ID for the non-salary-cost inserted.
  def test_insert_nsc(self):
    sample_nsc = ["Lab",100,12,60]
    result = Insert_All.insert_nsc(conn,sample_nsc)
    result1 = Insert_All.select_query(conn,'Select * from NonSalaryCosts where NSCID = '+str(result))
    sample_nsc.insert(0,result)
    self.assertEqual(result1[0],tuple(sample_nsc))
  
  # Test if insert_enrolment works.
  # The function returns the ID for the Enrolment inserted.
  def test_insert_enrolment(self):
    sample_enrol = [1,200,'Yes','No']
    result = Insert_All.insert_enrolment(conn,sample_enrol)
    result1 = Insert_All.select_query(conn,'Select * from enrolment where enrolmentID = '+str(result))
    sample_enrol.insert(0,result)
    self.assertEqual(result1[0],tuple(sample_enrol))
  
  # Test if insert_budget works.
  # The function returns the ID for the Budget inserted.
  def test_insert_budget(self):
    sample_budget = [1,6,"Yes","No"]
    result = Insert_All.insert_budget(conn,sample_budget)
    result1 = Insert_All.select_query(conn,'Select * from budget where budgetID = '+str(result))
    sample_budget.insert(0,result)
    self.assertEqual(result1[0],tuple(sample_budget))
  

  
 
  @classmethod
  def tearDownClass(self):
    #close database connection
    conn.close()
    # remove the database after test
    os.remove('Unit_Budget.db')


if __name__ == '__main__':
  unittest.main()