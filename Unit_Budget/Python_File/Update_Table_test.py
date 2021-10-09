from Update_Table import create_connection,update_unit
import os
import unittest

db = 'test.db'

class TestCreateTable(unittest.TestCase):
    def setUp(self):
        print("Prepare to test...")
        

    def tearDown(self):
        print("call teardown")
        os.remove(db)