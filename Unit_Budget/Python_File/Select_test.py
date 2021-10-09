from Select import select_all_tasks
import Insert_All_Liangbo_Version,Create_Table
import os
import unittest
import sqlite3
import sys
import io

db = 'Unit_Budget.db'

def stub_stdout(testcase_inst):
	stderr = sys.stderr
	stdout = sys.stdout

	def cleanup():
		sys.stderr = stderr
		sys.stdout = stdout

	testcase_inst.addCleanup(cleanup)
	sys.stderr = io.StringIO()
	sys.stdout = io.StringIO()

class TestSelect(unittest.TestCase):
    def setUp(self):
        print("Prepare to test...")
        Create_Table.Schema()
        
    def tearDown(self):
        print("call teardown")
        os.remove(db)

    def test_select_all_tasks(self):
        Insert_All_Liangbo_Version.sample_insert()
        sample_data = []   
        conn = sqlite3.connect(db) 
        stub_stdout(self) 
        select_all_tasks(conn) 
        self.assertEqual(str(sys.stdout.getvalue()), sample_data)  

if __name__ == '__main__':
    unittest.main()        
