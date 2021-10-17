from Update_Table import update_unit
import Insert_All_Liangbo_Version,Create_Table
import os
import unittest
import sqlite3

db = 'Unit_Budget.db'
Create_Table.Schema()

class TestCreateTable(unittest.TestCase):
    def test_update_unit(self):
        Insert_All_Liangbo_Version.sample_insert()
        conn = sqlite3.connect(db)
        c = conn.cursor()
        test_unit = ["CITS2021","SEM-2",2021,"1"]
        update_unit(conn, test_unit)
        self.assertEqual(list(c.execute('SELECT YEAR FROM Unit WHERE UNITCODE = ?',('CITS2021',))),[(2021,)])

    @classmethod
    def tearDownClass(cls):
        os.remove(db)

if __name__ == '__main__':
    unittest.main()   