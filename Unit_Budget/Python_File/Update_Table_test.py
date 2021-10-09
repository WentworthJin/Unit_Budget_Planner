from Update_Table import update_unit
import Insert_All_Liangbo_Version,Create_Table
import os
import unittest
import sqlite3

db = 'Unit_Budget.db'

class TestCreateTable(unittest.TestCase):
    def setUp(self):
        print("Prepare to test...")
        Create_Table.Schema()

    def tearDown(self):
        print("call teardown")
        os.remove(db)

    def test_update_unit(self):
        Insert_All_Liangbo_Version.sample_insert()
        conn = sqlite3.connect(db)
        c = conn.cursor()
        test_unit = []
        update_unit(conn, test_unit)
        self.assertEqual(len(c.execute('SELECT * FROM Unit WHERE UnitId = ?',('',)),''))

if __name__ == '__main__':
    unittest.main()   