import sqlite3
import sys
from sqlite3 import Error

TeachingCode = ["TeachingName"]
Unit = ["CITS2021","SEN-2",2020]
session = ["Lecture","Non-Mark"]
nsc = ["Lecture",6,10,60]
enrol = [1,200,'Yes','No']
budget = [1,6,"Yes","No"]
activities = [1,6,3,50,12]
oc = [1,6]
staff = [1,"Racheal","Lecture"]

#create a database connection to a SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn


#Insert data into Unit table
def insert_unit(conn, unit):
    sql = ''' INSERT INTO Unit(UnitCode,Semester,Year)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, unit)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, unit)
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into TeachingCode table
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

#Insert data into Session table
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

#Insert data into NonSalaryCosts table
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

#Insert data into Enrolment table
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

#Insert data into Budget table
def insert_budget(conn, budget):
    sql = ''' Insert into Budget(UnitID,Cost,IsEstimated,IsLastSemester)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, budget)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, budget)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into Activities table
def insert_activities(conn, activities):
    sql = ''' Insert into Activities(UnitID,StaffID,SessionID,HourlyRate,Hour)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, activities)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, activities)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into OtherCost table
def insert_oc(conn, oc):
    sql = ''' Insert into OtherCost(NSCID,UnitID)
              VALUES(?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, oc)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, oc)
      conn.commit()
    else:
      conn.commit()
      return cur.lastrowid

#Insert data into Staff table
def insert_staff(conn, staff):
    sql = ''' Insert into Staff(TeachingID,Name,Position)
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
      insert_activities(conn, activities)

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

