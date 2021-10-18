from route import app
import unittest
import json


class FlaskTestCase(unittest.TestCase):
  
  # test to ensure that flask set up correctly 
  def test_flask(self):
    test = app.test_client(self)
    response = test.get("/", content_type="html/text")
    self.assertEqual(response.status_code,200)
    
  # test to ensure that correctly render the summary report page 
  def test_summary_report(self):
    test = app.test_client(self)
    response = test.get("/get", content_type="html/text")
    self.assertTrue(b'Summary Report' in response.data)
    
  # test to ensure that back button redirect to the home page 
  def test_back_button(self):
    test = app.test_client(self)
    response = test.get("/", follow_redirects = True)
    self.assertIn(b'Welcome back to the Unit Budget Planner!', response.data)
    
  # ensure that the route return a json with summary data 
  def test_all_data(self):
    test = app.test_client(self)
    response = test.get("/get_all_data")
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(data[0], ['CITS5503', 155.0, '2', 2020, 2, 7030.0, 1500.0, 5561, 8, 6, 155.0, 72, 77])
    
  # ensure that route return the correct data for each employee budget
  def test_employee_data(self):
    test = app.test_client(self)
    response = test.get("/employee_budget")
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(data[0], ['David Glance', 'CITS5503', '2', 2020, 2550.0])
  
  # ensure that route return the correct data for workload and total cost and unit 
  def test_workload_data(self):
    test = app.test_client(self)
    response = test.get("/workload")
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(data[0],['CITS5503', 155.0, 7030.0])
    
  # ensure that route return the correct comment according to semester
  def test_comment_semester(self):
    test = app.test_client(self)
    response = test.get('/comment?semester=2')
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(data[0],["CITS5503","Lecuture is 4 hours/week"])
    
  # ensure that route return the correct comment according to unit
  def test_comment_unit(self):
    test = app.test_client(self)
    response = test.get('/comment?unitcode=CITS5503')
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(data[0],["CITS5503","Lecuture is 4 hours/week"])
    
  # ensure that route return the correct comment according to year
  def test_comment_unit(self):
    test = app.test_client(self)
    response = test.get('/comment?year=2021')
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(data[0],["CITS1101","Lecuture is 4 hours/week"])
  
  # ensure that route return the correct comment according to year, unit and semester
  def test_comment_all(self):
    test= app.test_client(self)
    response = test.get('/comment?year=2020&semester=2&unitcode=CITS5503')
    data = json.loads(response.get_data(as_text=True))
    self.assertEqual(data[0],["CITS5503","Lecuture is 4 hours/week"])
    
  
if __name__=="__main__":
  unittest.main(verbosity=2)