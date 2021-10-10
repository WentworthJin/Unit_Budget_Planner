import unittest
from Create_Table import Schema,create_connection,create_table
import os

db = 'Unit_Budget.db'

class TestCreateTable(unittest.TestCase):    
    def test_schema(self):
        Schema()
        self.assertIsNotNone(create_connection(db))

    def test_create_table(self):
        con = create_connection(db)
        self.assertIsNone(create_table(con,'''CREATE TABLE IF NOT EXISTS Test'''))
    
    @classmethod
    def tearDownClass(cls):
        os.remove(db)
        
if __name__ == '__main__':
    unittest.main()        
