import unittest
from Delete_Data import create_connection,delete_task,delete_all_unit
import os

db = 'test.db'

class TestCreateTable(unittest.TestCase):
    def setUp(self):
        print("Prepare to test...")
        

    def tearDown(self):
        print("call teardown")
        os.remove(db)