import Insert_All_Liangbo_Version,Create_Table
import os
import unittest
import sqlite3

db = 'Unit_Budget.db'
Create_Table.Schema()
conn = sqlite3.connect(db)

class Test_Insert(unittest.TestCase):
    def test_Insert_Unit(self):
        sample_unit = ["Computing","CITS2021","SEM-2",2020,"Fail"]
        result = Insert_All_Liangbo_Version.insert_unit(conn,sample_unit)
        self.assertEqual(result,1)

    def test_Insert_TeachingCode(self):
        sample_TeachingCode = ["ORAA"]
        result = Insert_All_Liangbo_Version.insert_teachingcode(conn,sample_TeachingCode)
        self.assertEqual(result,1)

    def test_Insert_Session(self):
        sample_session = ["Lecture","NM"]
        result = Insert_All_Liangbo_Version.insert_session(conn,sample_session)
        self.assertEqual(result,1)

    def test_Insert_NSC(self):
        sample_nsc = ["Lecture",6,10,60]
        result = Insert_All_Liangbo_Version.insert_nsc(conn,sample_nsc)
        self.assertEqual(result,1)

    def test_Insert_Enrolment(self):
        sample_enrolment = [1,200,'Yes','No']
        result = Insert_All_Liangbo_Version.insert_enrolment(conn,sample_enrolment)
        self.assertEqual(result,1)

    def test_Insert_Budget(self):
        sample_budget = [1,30000,'YES','NO']
        result = Insert_All_Liangbo_Version.insert_budget(conn,sample_budget)
        self.assertEqual(result,1)

    def test_Insert_Activities(self):
        sample_activity = [1,1,1,4,0.25,30,60,"Good"]
        result = Insert_All_Liangbo_Version.insert_activities(conn,sample_activity)
        self.assertEqual(result,1)

    def test_Insert_OC(self):
        sample_oc = [1,6,"Good"]
        result = Insert_All_Liangbo_Version.insert_oc(conn,sample_oc)
        self.assertEqual(result,1)

    def test_Insert_Staff(self):
        sample_staff = [1,"Racheal","Lecture"]
        result = Insert_All_Liangbo_Version.insert_staff(conn,sample_staff)
        self.assertEqual(result,1)
    
    @classmethod
    def tearDownClass(cls):
        os.remove(db)

if __name__ == '__main__':
    unittest.main()   