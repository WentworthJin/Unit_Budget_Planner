import unittest
from getFunction import select_NSCID,select_StaffID,select_TeachingCode
import os
import Insert_All_Liangbo_Version,Create_Table
import sqlite3

db = 'Unit_Budget.db'
Create_Table.Schema()
Insert_All_Liangbo_Version.sample_insert()

class Test_get_Function(unittest.TestCase):
    def test_select_NSCID(self):
        sample_NSCName = 'Lecture'   
        conn = sqlite3.connect(db)
        self.assertEqual(select_NSCID(conn,sample_NSCName),'')

    def test_select_StaffID(self):
        sample_Name = 'Racheal'   
        conn = sqlite3.connect(db)
        self.assertEqual(select_StaffID(conn,sample_Name),'')

    def test_select_TeachingCode(self):
        sample_TeachingCode = 'ORAA'   
        conn = sqlite3.connect(db)
        self.assertEqual(select_TeachingCode(conn,sample_TeachingCode),'')

    @classmethod
    def tearDownClass(cls):
        os.remove(db)

if __name__ == '__main__':
    unittest.main() 