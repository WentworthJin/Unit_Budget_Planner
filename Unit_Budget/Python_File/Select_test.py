from Select import create_connection,select_all_tasks
import os
import unittest

db = 'test.db'

class TestCreateTable(unittest.TestCase):
    def setUp(self):
        print("Prepare to test...")
        

    def tearDown(self):
        print("call teardown")
        os.remove(db)