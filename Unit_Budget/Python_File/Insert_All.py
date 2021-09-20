import sqlite3
import sys
import pandas as pd
import numbers
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


#Insert data into OtherCost table
def insert_otherCost(conn, otherCost):
    sql = ''' Insert into OtherCost(NSCID,UnitID)
              VALUES(?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, otherCost)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, otherCost)
      conn.commit()
      return cur.lastrowid



#Insert data into Staff table
def insert_staff(conn, staff):
    sql = ''' Insert into Staff(TeachingID,Name,Postion)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    data_check=cur.execute(sql, staff)
    # Check if data already exist
    if data_check is None:
      cur.execute(sql, staff)
      conn.commit()
      return cur.lastrowid

# retrieve information from excel file to dataframe 
def get_details(file):
  unit_detail = pd.read_excel(file,usecols ="A:L",header =8,nrows=5)
  unit_strcture = pd.read_excel(file,usecols ="A:J",header =29,nrows=13)
  resourcing = pd.read_excel(file,usecols ="A:L",header =46,nrows=9)
  NSC = pd.read_excel(file,usecols ="A:F",header =62,nrows=4)
  return unit_detail,unit_strcture,resourcing,NSC

# check if a session is makring session or not 
def check_session(SessionName):
  if 'mark' in SessionName.lower():
    return 'M'
  else:
    return 'NM'

# check if this value is numberic
def check_numbers(number):
  return isinstance(number, numbers.Number)



def select_StaffID(conn,Name):

  QueryTemplate = '''Select StaffID From Staff Where Name = {0};'''

  query = QueryTemplate.format(Name)

  cur = conn.cursor()
  cur.execute(query)

  rows = cur.fetchall()

  return rows[0][0]


def select_TeachingCode(conn,TeachingName):

  QueryTemplate = '''Select TeachingCode From TeachingCode Where TeachingName = {0};'''

  query = QueryTemplate.format(TeachingName)

  cur = conn.cursor()
  cur.execute(query)

  rows = cur.fetchall()

  return rows[0][0]

#s = select_StaffID(conn,'''"Racheal"''') 





def main():
  pd.set_option("max_columns", 10)
  excel_file ="CITS1001_Sem1,2021 budget v3.xlsx"
  unit_detail,unit_strcture,resourcing,NSC = get_details(excel_file)

  thisyear_detail = unit_detail.iloc[:,3:7]

  lastyear_detail = unit_detail.iloc[:,8:12]


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
      UnitID = insert_unit(conn,Unit)

      #Insert TeachingCode table
      for TeachingName in teachingcodes:
        TeachingCode = [TeachingName]
        insert_teachingcode(conn,TeachingCode)


      #Insert Staff table
      for i in range(len(teachingcodes)):
        teachingID = select_StaffID(conn,resourcing.iloc[0:7,3][i])
        teacherName = resourcing.iloc[0:7,0][i]
        teacherPostion = resourcing.iloc[0:7,1][i]
        staff = (teachingID,teacherName,teacherPostion)
        insert_session(conn,staff)


      #Insert Session table
      for SessionName in sessionNames:
        SessionType = check_session(SessionName)
        session = (SessionName,SessionType)
        insert_session(conn,session)


      #Insert NonSalaryCost table & OtherCost Table
      for i in range(len(NSCCost)):
        NSCName = NSCNames[i]
        Hours = NSCHours[i]
        CostPerHour = NSCRates[i]
        TotalCost = int(NSCCost[i])
        nsc = (NSCName,Hours,CostPerHour,TotalCost)
        NSCID = insert_nsc(conn,nsc)

        otherCost = (NSCID,UnitID)
        insert_session(conn,otherCost)

      #Insert Enrolment table & Budget Table
      for i in range(len(thisyear_detail.index)):
        if 'estimated enrolment' in thisyear_detail.iloc[:,0][i].lower():
          if check_numbers(thisyear_detail.iloc[:,3][i]):
            enrol = (UnitID,thisyear_detail.iloc[:,3][i],'Yes','No')
            insert_enrolment(conn,enrol)
        if 'budget' in thisyear_detail.iloc[:,0][i].lower():
          if check_numbers(thisyear_detail.iloc[:,3][i]):
            budget = (UnitID,thisyear_detail.iloc[:,3][i],'Yes','No')
            insert_budget(conn,budget)

      for i in range(len(lastyear_detail.index)):
        if 'estimated enrolment' in lastyear_detail.iloc[:,0][i].lower():
          if check_numbers(lastyear_detail.iloc[:,3][i]):
            enrol = (UnitID,lastyear_detail.iloc[:,3][i],'Yes','Yes')
            insert_enrolment(conn,enrol)

        if 'actual enrolment' in lastyear_detail.iloc[:,0][i].lower():
          if check_numbers(lastyear_detail.iloc[:,3][i]):
            enrol = (UnitID,lastyear_detail.iloc[:,3][i],'No','Yes')
            insert_enrolment(conn,enrol)

        if 'budget' in lastyear_detail.iloc[:,0][i].lower():
          if check_numbers(lastyear_detail.iloc[:,3][i]):
            budget = (UnitID,lastyear_detail.iloc[:,3][i],'Yes','Yes')
            insert_enrolment(conn,enrol)

        if 'actual expense' in lastyear_detail.iloc[:,0][i].lower():
          if check_numbers(lastyear_detail.iloc[:,3][i]):
            budget = (UnitID,lastyear_detail.iloc[:,3][i],'No','Yes')
            insert_enrolment(conn,enrol)


    print("Dummy Unit data has been inserted")

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()

