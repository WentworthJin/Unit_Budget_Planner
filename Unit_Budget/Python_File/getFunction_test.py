import unittest
from getFunction import select_NSCID,select_StaffID,select_TeachingCode
import os
import Insert_All_Liangbo_Version,Create_Table
import sqlite3

db = 'Unit_Budget.db'
Create_Table.Schema()

class Test_get_Function(unittest.TestCase):
    def test_select_NSCID(self):
        Insert_All_Liangbo_Version.sample_insert()
        sample_NSCName = ''   
        conn = sqlite3.connect(db)
        self.assertEqual(select_NSCID(conn,sample_NSCName),'')

    def test_select_StaffID(self):
        Insert_All_Liangbo_Version.sample_insert()
        sample_Name = ''   
        conn = sqlite3.connect(db)
        self.assertEqual(select_StaffID(conn,sample_Name),'')

    def test_select_TeachingCode(self):
        Insert_All_Liangbo_Version.sample_insert()
        sample_TeachingName = ''   
        conn = sqlite3.connect(db)
        self.assertEqual(select_TeachingCode(conn,sample_TeachingName),'')

    @classmethod
    def tearDownClass(cls):
        os.remove(db)

if __name__ == '__main__':
    unittest.main() 