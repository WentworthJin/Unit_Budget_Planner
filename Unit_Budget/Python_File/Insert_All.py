import sqlite3
import sys
import pandas as pd
from sqlite3 import Error

TeachingCode = ["TeachingName"]
Unit = ["CITS2021","SEN-2",2020]
session = ["Lecture","Non-Mark"]
nsc = ["Lecture",6,10,60]
enrol = [1,200,'Yes','No']
budget = [1,6,"Yes","No"]

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
      return cur.lastrowid

def get_details(file):
  unit_detail = pd.read_excel(file,usecols ="A:B",header =8,nrows=5)
  unit_strcture = pd.read_excel(file,usecols ="A:J",header =29,nrows=13)
  resourcing = pd.read_excel(file,usecols ="A:L",header =46,nrows=9)
  NSC = pd.read_excel(file,usecols ="A:F",header =62,nrows=4)
  return unit_detail,unit_strcture,resourcing,NSC


def check_session(SessionName):
  if 'mark' in SessionName.lower():
    return 'M'
  else:
    return 'NM'




def main():
  pd.set_option("max_columns", 10)
  excel_file ="CITS1001_Sem1,2021 budget v3.xlsx"
  unit_detail,unit_strcture,resourcing,NSC = get_details(excel_file)

  UnitCode =unit_detail.iloc[0,1]
  Semester=unit_detail.iloc[1,1]
  Year =unit_detail.iloc[4,1]

  teachingcodes = resourcing.iloc[0:7,3]

  sessionNames =unit_strcture.iloc[0:12,0]

  NSCNames = NSC.iloc[:3,0]
  NSCHours = NSC.iloc[:3,3]
  NSCRates = NSC.iloc[:3,4]
  NSCCost = NSC.iloc[:3,5]

  try:
    database = "Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    with conn:

      #Insert Unit table
      Unit = (UnitCode,Semester,Year)
      insert_unit(conn,Unit)

      #Insert TeachingCode table
      for TeachingName in teachingcodes:
        TeachingCode = (TeachingName)
        insert_teachingcode(conn,TeachingCode)

      #Insert Session table
      for SessionName in sessionNames:
        SessionType = check_session(SessionName)
        session = (SessionName,SessionType)
        insert_session(conn,session)


      #Insert NonSalaryCost table
      for i in range(len(NSCCost)):
        NSCName = NSCNames[i]
        Hours = NSCHours[i]
        CostPerHour = NSCRates[i]
        TotalCost = NSCCost[i]
        nsc = (NSCName,Hours,CostPerHour,TotalCost)
        insert_nsc(conn,nsc)

      #Insert Enrolment table
      enrol = (UnitID,EnrolmentNumber,IsEstimated,IsLastSemester)
      insert_enrolment(conn,enrol)

      #Insert Budget table
      #budget = (UnitID,Cost,IsEstimated,IsLastSemester)
      insert_budget(conn,budget)

    print("Dummy Unit data has been inserted")

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()

