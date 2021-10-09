import Insert_All_Liangbo_Version,Insert_All,Insert_Budget,Insert_Enrolment,Insert_NonSalaryCost,Insert_Session,Insert_TeachingCode,Insert_Unit
import os
import unittest

db = 'test.db'

class TestCreateTable(unittest.TestCase):
    def setUp(self):
        print("Prepare to test...")
        

    def tearDown(self):
        print("call teardown")
        os.remove(db)