import unittest
from Delete_Data import delete_task,delete_all_unit
import Insert_All_Liangbo_Version,Create_Table
import os
import sqlite3

db = 'Unit_Budget.db'
Create_Table.Schema()

class TestDeleteData(unittest.TestCase):
    def test_delete_task(self):
        Insert_All_Liangbo_Version.sample_insert()
        test_task = 'CITS2021'
        conn = sqlite3.connect(db)
        delete_task(conn,test_task)
        c = conn.cursor()
        self.assertEqual(0,len(c.execute('SELECT * FROM Unit WHERE UnitId = ?',(test_task,))))

    def test_delete_all_unit(self):
        Insert_All_Liangbo_Version.sample_insert()
        conn = sqlite3.connect(db)        
        delete_all_unit(conn)        
        c = conn.cursor()
        self.assertEqual(0,len(c.execute('SELECT * FROM Unit')))

    @classmethod
    def tearDownClass(cls):
        os.remove(db)
        
if __name__ == '__main__':
    unittest.main()    