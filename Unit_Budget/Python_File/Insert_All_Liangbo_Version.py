import sqlite3
import sys
from sqlite3 import Error

activity = [1,1,1,4,0.25,30,60]
budget = [1,30000,'YES','NO']
enrol = [1,200,'Yes','No']
nsc = ["Lecture",6,10,60]
oc = [1,6]
session = ["Lecture","NM"]
staff = [1,"Racheal","Lecture"]
TeachingCode = ["ORAA"]
Unit = ["Computing","CITS2021","SEM-2",2020]

'''
    Functionality: The Insert_All_Liangbo_Version.py.py is a framework that provides various functions for other users 
                   to use, in order to insert data into the database. 
    
    You can run this file by: Import the functions inside this file
    
    Parameters: Table data
    
    Result: Insert the Table data into the database

    Testing: Refer to the " test_Insert_All.py " testing file, in order to test if the function can 
             correctly insert data into the Unit_Budget.db.

'''

#create a database connection to a SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn


#Insert data into Activities table
activity = [1,1,1,4,0.25,30,60]
def insert_activities(conn, act):
    sql = '''INSERT INTO Activities (UnitID, StaffID, SessionID, HourPerSession, MarkingHourPS, PayRate, Hour) 
    VALUES(?, ?, ?, ?, ?, ?, ?);'''
    cur = conn.cursor()
    data_check=cur.execute(sql, act)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, act)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into Budget table
budget = [1,30000,'YES','NO']
def insert_budget(conn, budget):
    sql = ''' INSERT INTO Budget(UnitID, Cost, IsEstimated, IsLastSemester) 
    VALUES(?,?,?,?); '''
    cur = conn.cursor()
    data_check=cur.execute(sql, budget)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, budget)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into Enrolment table
enrol = [1,200,'Yes','No']
def insert_enrolment(conn, enrol):
    sql = ''' Insert into Enrolment(UnitID,EnrolmentNumber,IsEstimated,IsLastSemester)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, enrol)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, enrol)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into NonSalaryCosts table
nsc = ["Lecture",6,10,60]
def insert_nsc(conn, nsc):
    sql = ''' Insert into NonSalaryCosts(NSCName,Hours,CostPerHour,TotalCost)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, nsc)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, nsc)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into OtherCost table
oc = [1,6]
def insert_oc(conn, oc):
    sql = ''' INSERT INTO OtherCost(NSCID, UnitID) 
    VALUES (?,?); '''
    cur = conn.cursor()
    data_check=cur.execute(sql, oc)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, oc)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into Session table
session = ["Lecture","NM"]
def insert_session(conn, session):
    sql = ''' Insert into Session(SessionName,SessionType)
              VALUES(?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, session)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, session)
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into Staff table
staff = [1,"Racheal","Lecture"]
def insert_staff(conn, staff):
    sql = ''' Insert into Staff(TeachingCode,Name,Position)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, staff)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, staff)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into TeachingCode table
TeachingCode = ["ORAA"]
def insert_teachingcode(conn, TeachingCode):
    sql = ''' Insert into TeachingCode(TeachingName)
              VALUES(?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, TeachingCode)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, TeachingCode)
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into Unit table
Unit = ["Computing","CITS2021","SEM-2",2020]
def insert_unit(conn, unit):
    sql = ''' INSERT INTO Unit(UnitName,UnitCode,Semester,Year)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, unit)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, unit)
    else:
      conn.commit()
      return cur.lastrowid

def sample_insert():

  try:
    database = "Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    with conn:

      #Insert Unit table
      #Unit = (UnitCode,Semester,Year)
      insert_unit(conn,Unit)

      #Insert TeachingCode table
      #TeachingCode = (TeachingName)
      insert_teachingcode(conn,TeachingCode)

      #Insert Session table
      #session = (SessionName,SessionType)
      insert_session(conn,session)

      #Insert NonSalaryCost table
      #nsc = (NSCName,Hours,CostPerHour,TotalCost)
      insert_nsc(conn,nsc)

      #Insert Enrolment table
      #enrol = (UnitID,EnrolmentNumber,IsEstimated,IsLastSemester)
      insert_enrolment(conn,enrol)

      #Insert Budget table
      #budget = (UnitID,Cost,IsEstimated,IsLastSemester)
      insert_budget(conn,budget)

      # Insert Activities table
      # activities = (UnitID, StaffID, SessionID, HourlyRate, Hour)
      insert_activities(conn, activity)

      # Insert Staff table
      # staff = (TeachingID, Name, Position)
      insert_staff(conn,staff)

      # Insert Other Cost table
      # oc = (NSCID, UnitID)
      insert_oc(conn, oc)

    print("All Dummy data has been inserted")

  except Error as e:
    print(e)

if __name__ == '__main__':
  sample_insert()

