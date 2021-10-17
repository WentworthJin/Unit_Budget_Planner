from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from Create_Table import Schema
from Insert_All_Liangbo_Version import sample_insert
import sqlite3 
import os.path

# Initilize the Database
Schema()

# Insert mock data
# sample_insert()

# File Type Limit
ALLOWED_EXTENSIONS = {'xlsx'}

# Specify Path
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, './uploads')

app = Flask(__name__,template_folder='../dist',static_folder='../src')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# get the absolute path for the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
# get the whole path to database
db_path = os.path.join(BASE_DIR, "BudgetSample.db")

@app.route("/", methods=["GET"])
def render():
  return render_template("index.html")

def buildWhereClause(data): 
  data = request.args.to_dict()
  params = data.keys()
  s1 = 'U.UnitCode ="{}" '.format(data['unitcode']) if 'unitcode' in params else ''
  s2 = 'U.Year = ' + data['year'] if 'year' in params else ''
  s3 = 'U.Semester = ' + data['semester'] if 'semester' in params else ''
  s = list()
  for x in [s1, s2, s3]:
      if x:
          s.append(x)
  queryStrings = ' and '.join(s) 
  return queryStrings



@app.route("/get", methods=["GET"])
def get_all_data():
  
  """The function is used to get the summary data from database and send to client side 

   Parameters: There is no parameter needed for this one. 
   """
  
  query = 'Select U.UnitCode, SUM(A.Hour) AS TotalLoad, U.Semester,U.Year, \
          (Select COUNT(DISTINCT P.Name) \
          From Activities A JOIN Staff P USING (StaffID) \
          JOIN Unit R USING (UnitID) \
          Where R.UnitCode = U.UnitCode \
          ) AS Num_of_Staff, \
          SUM(A.Hour * A.PayRate) AS StaffCost, \
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
          Group by N.UnitID) AS Total_WorkLoad, \
          (Select En.EnrolmentNumber \
          FROM Enrolment En \
          JOIN Budget B USING (UnitID) \
          Where En.IsEstimated = "YES" and En.IsLastSemester = "NO" and En.UnitID = U.UnitID ) AS Enrolment_number, \
          (Select B.cost / En.EnrolmentNumber from Budget B JOIN Enrolment En USING (UnitID) \
          Where B.IsEstimated="YES" and B.IsLastSemester="NO" and En.IsEstimated="YES" \
          and En.IsLastSemester="NO" and En.UnitID = U.UnitID) AS Cost_per_student \
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
  """The function is used to get the  main data from database and send to client side 
   Parameters: There is no parameter needed for this one. 
   """
  queryStrings = buildWhereClause(request.args.to_dict())
  con = sqlite3.connect(db_path)
  cur = con.cursor()
  sql = 'Select U.UnitCode, SUM(A.Hour) AS TotalLoad, U.Semester,U.Year, \
                      (Select COUNT(DISTINCT P.Name) \
                      From Activities A JOIN Staff P USING (StaffID) \
                      JOIN Unit R USING (UnitID) \
                      Where R.UnitCode = U.UnitCode \
                      ) AS Num_of_Staff, \
                      SUM(A.Hour * A.PayRate) AS StaffCost, \
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
                      Group by N.UnitID) AS Total_WorkLoad, \
                      (Select En.EnrolmentNumber \
                      FROM Enrolment En \
                      JOIN Budget B USING (UnitID) \
                      Where En.IsEstimated = "YES" and En.IsLastSemester = "NO" and En.UnitID = U.UnitID ) AS Enrolment_number, \
                      (Select B.cost / En.EnrolmentNumber from Budget B JOIN Enrolment En USING (UnitID) \
                      Where B.IsEstimated="YES" and B.IsLastSemester="NO" and En.IsEstimated="YES" \
                      and En.IsLastSemester="NO" and En.UnitID = U.UnitID) AS Cost_per_student \
                      From Activities A JOIN Staff S USING (StaffID)  \
                          JOIN Session E USING (SessionID) \
                          JOIN Unit U USING (UnitID) \
                      '         
  if queryStrings:
    sql = sql + ''' where ''' + queryStrings    

  cur.execute(sql + " Group By U.UnitID ") 
  result = cur.fetchall()
  con.close()
  return jsonify(result)


# route to get each employees in each unit budget
@app.route("/employee_budget", methods=["GET"])
def get_employee_budget():
  """The function is used to get the employees budget data from database and send to client side 

   Parameters: There is no parameter needed for this one. 
   """
  queryStrings = buildWhereClause(request.args.to_dict())
  con = sqlite3.connect(db_path)
  cur = con.cursor()
  sql = "Select S.Name, U.UnitCode, U.Semester, U.Year, SUM(A.Hour*A.HourlyRate) AS TotalCost \
        From Activities A JOIN Staff S USING (StaffID) \
        JOIN Session E USING (SessionID) \
        JOIN Unit U USING (UnitID) "
  if queryStrings:
    sql = sql + ''' where ''' + queryStrings         
  cur.execute(sql + " Group by S.StaffID ") 
  result = cur.fetchall()
  con.close()
  return jsonify(result)

# get workload and total cost for each unit 
@app.route("/workload", methods=["GET"])
def get_semester_budget():
  """The function is used to get the workload and budget data from database and send to client side 

   Parameters: There is no parameter needed for this one. 
   """
  queryStrings = buildWhereClause(request.args.to_dict())
  con = sqlite3.connect(db_path)
  cur = con.cursor()
  sql = "Select U.UnitCode, SUM(A.Hour) AS TotalLoad, SUM(A.Hour * A.HourlyRate) AS StaffCost \
              From Activities A JOIN Staff S USING (StaffID) \
                JOIN Session E USING (SessionID) \
                JOIN Unit U USING (UnitID) \
              "
  if queryStrings:
    sql = sql + ''' where ''' + queryStrings
  sql = sql + " Group By U.UnitID "
  cur.execute(sql)
  result = cur.fetchall()
  con.close()
  return jsonify(result)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route("/comment", methods=["GET"])
def get_comment():
  requestStrings = buildJoinClause(request.args.to_dict())
  con = sqlite3.connect(db_path)
  cur = con.cursor()
  sql = "Select U.UnitCode, A.Comment \
        from Activities A \
        JOIN Unit U USING (UnitID)"
  if requestStrings:
    sql = sql + ''' where ''' + requestStrings 
  sql = sql + " and A.Comment IS NOT NULL"
  cur.execute(sql)
  result = cur.fetchall()
  con.close()
  return jsonify(result)

@app.route("/table",methods=['GET','POST'])
def upload_file():
  try:
    if request.method == 'POST':
      if 'filename' not in request.files:
        return render()
      file = request.files['filename']
      if file.filename == '':
            return render()
      if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        Unit_ID = filename [0:8]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # Insert mock data
    ID = 'CITS4401'
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
    rows = cur.fetchall()
    for row in rows:
      if row[0] == ID:
        data = row
    return render_template('table.html',data = data)
  except:
    return render()

@app.route('/customSqlQuery', methods=['POST'])
def sqlquery():
    try:
        print(request.form.to_dict())
        sql = request.form['sql']
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute(sql)
        col_name_list = [tuple[0] for tuple in c.description]
        content = c.fetchall()
        conn.commit()
        conn.close()
        r = {'success':'ture','data':list()}
        for row in content:
            d = dict(zip(col_name_list, row))
            r['data'].append(d)
        return jsonify(r)
    except:
        return {'success':'false'}    

if __name__=="__main__":
  app.run(host='127.0.0.1', port=5000,debug=True)


  



