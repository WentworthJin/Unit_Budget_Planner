from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
import Create_Table
import sqlite3 
import os.path


app = Flask(__name__,template_folder='../dist',static_folder='../src')
app.config['./Upload_file']

# get the absolute path for the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
# get the whole path to database
db_path = os.path.join(BASE_DIR, "BudgetSample (1).db")

@app.route("/", methods=["GET"])
def render():
  return render_template("index.html")


@app.route("/get", methods=["GET"])
def get_all_data():
  
  query = 'Select U.UnitCode, SUM(A.Hour) AS TotalLoad, U.Semester,U.Year, \
          (Select COUNT(DISTINCT P.Name) \
          From Activities A JOIN Staff P USING (StaffID) \
          JOIN Unit R USING (UnitID) \
          Where R.UnitCode = U.UnitCode \
          ) AS Num_of_Staff, \
          SUM(A.Hour * A.HourlyRate) AS StaffCost, \
          (Select SUM(N.TotalCost) \
          From OtherCost O JOIN NonSalaryCosts N USING (NSCID) \
          JOIN UNIT Z USING (UnitID) \
          Where Z.UnitID = U.UnitID \
          Group by Z.UnitID) AS NonSalaryCost, \
          (Select B.Cost \
          From Unit G JOIN Budget B USING (UnitID) \
          Where IsEstimated = "YES" and B.IsLastSemester = "NO" and G.UnitID = U.UnitID ) AS Budget, \
          (Select COUNT(*) \
          From Activities A JOIN Unit P USING (UnitID) \
          Where P.UnitID = U.UnitID \
          Group by P.UnitID) AS TotalActivities, \
          (Select COUNT(*) \
          From OtherCost O JOIN Unit L USING (UnitID) \
          JOIN NonSalaryCosts USING (NSCID) \
          Where L.UnitID = U.UnitID \
          Group by L.UnitID) AS Total_Number_of_NSC, \
          (Select SUM(A.Hour) \
          From Activities A JOIN Unit N USING (UnitID) \
          Where N.UnitID = U.UnitID \
          Group by N.UnitID) AS Total_WorkLoad \
          From Activities A JOIN Staff S USING (StaffID)  \
                                        JOIN Session E USING (SessionID) \
                                        JOIN Unit U USING (UnitID) \
          Group By U.UnitID'

  # connect to database 
  con = sqlite3.connect(db_path)
  # create a cursor method to perform sql command 
  cur = con.cursor()
  # try to get the column names
  cursor = con.execute(query)
  names = [description[0] for description in cursor.description]
  cur.execute(query)
  rows = cur.fetchall()
  # clost the connection to database
  con.close()
  
  return render_template("result.html", rows=rows, names=names)

@app.route("/get_all_data", methods=["GET"])
def get_main_data():
  con = sqlite3.connect(db_path)
  cur = con.cursor()
  cur.execute('Select U.UnitCode, SUM(A.Hour) AS TotalLoad, U.Semester,U.Year, \
                      (Select COUNT(DISTINCT P.Name) \
                      From Activities A JOIN Staff P USING (StaffID) \
                      JOIN Unit R USING (UnitID) \
                      Where R.UnitCode = U.UnitCode \
                      ) AS Num_of_Staff, \
                      SUM(A.Hour * A.HourlyRate) AS StaffCost, \
                      (Select SUM(N.TotalCost) \
                      From OtherCost O JOIN NonSalaryCosts N USING (NSCID) \
                      JOIN UNIT Z USING (UnitID) \
                      Where Z.UnitID = U.UnitID \
                      Group by Z.UnitID) AS NonSalaryCost, \
                      (Select B.Cost \
                      From Unit G JOIN Budget B USING (UnitID) \
                      Where IsEstimated = "YES" and B.IsLastSemester = "NO" and G.UnitID = U.UnitID ) AS Budget, \
                      (Select COUNT(*) \
                      From Activities A JOIN Unit P USING (UnitID) \
                      Where P.UnitID = U.UnitID \
                      Group by P.UnitID) AS TotalActivities, \
                      (Select COUNT(*) \
                      From OtherCost O JOIN Unit L USING (UnitID) \
                      JOIN NonSalaryCosts USING (NSCID) \
                      Where L.UnitID = U.UnitID \
                      Group by L.UnitID) AS Total_Number_of_NSC, \
                      (Select SUM(A.Hour) \
                      From Activities A JOIN Unit N USING (UnitID) \
                      Where N.UnitID = U.UnitID \
                      Group by N.UnitID) AS Total_WorkLoad \
                      From Activities A JOIN Staff S USING (StaffID)  \
                                                    JOIN Session E USING (SessionID) \
                                                    JOIN Unit U USING (UnitID) \
                      Group By U.UnitID')
  result = cur.fetchall()
  return jsonify(result)

# route to get each employees in each unit budget
@app.route("/employee_budget", methods=["GET"])
def get_employee_budget():
  con = sqlite3.connect(db_path)
  cur = con.cursor()
  cur.execute("Select S.Name, U.UnitCode, U.Semester, U.Year, SUM(A.Hour*A.HourlyRate) AS TotalCost \
              From Activities A JOIN Staff S USING (StaffID) \
                JOIN Session E USING (SessionID) \
                JOIN Unit U USING (UnitID) \
              Group by S.StaffID ") 
  result = cur.fetchall()
  return jsonify(result)

@app.route("/table",methods=['GET','POST'])
def gettable():
  return render_template("table.html")

if __name__=="__main__":
  app.run(host='127.0.0.1', port=5000,debug=True)


  



