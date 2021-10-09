import unittest
from getFunction import create_connection,select_NSCID,select_StaffID,select_TeachingCode
import os

db = 'test.db'

class TestCreateTable(unittest.TestCase):
    def setUp(self):
        print("Prepare to test...")
        

    def tearDown(self):
        print("call teardown")
        os.remove(db)