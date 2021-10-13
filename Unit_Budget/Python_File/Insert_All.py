import sqlite3
import sys
import pandas as pd
import numbers
import math
import Configure
from sqlite3 import Error


#create a database connection to a SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return conn


def select_query(conn,query):
  cur = conn.cursor()
  cur.execute(query)
  return cur.fetchall()


def insert_activities(conn, act):
    sql = '''INSERT OR IGNORE INTO Activities (UnitID, StaffID, SessionID, HourPerSession, MarkingHourPS, PayRate, Hour) 
    VALUES(?, ?, ?, ?, ?, ?, ?);'''
    cur = conn.cursor()
    cur.execute(sql, act)
    conn.commit()
    #return cur.lastrowid

#Insert data into Budget table
def insert_budget(conn, budget):
    sql = ''' INSERT OR IGNORE INTO Budget(UnitID, Cost, IsEstimated, IsLastSemester) 
    VALUES(?,?,?,?); '''
    cur = conn.cursor()
    cur.execute(sql, budget)
    conn.commit()


#Insert data into Enrolment table
def insert_enrolment(conn, enrol):
    sql = ''' Insert OR IGNORE into Enrolment(UnitID,EnrolmentNumber,IsEstimated,IsLastSemester)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, enrol)
    conn.commit()


#Insert data into NonSalaryCosts table
def insert_nsc(conn, nsc):
    sql = ''' Insert OR IGNORE into NonSalaryCosts(NSCName,Hours,CostPerHour,TotalCost)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, nsc)
    conn.commit()
    return cur.lastrowid

#Insert data into OtherCost table
def insert_oc(conn, oc):
    sql = ''' INSERT OR IGNORE INTO OtherCost(NSCID, UnitID) 
    VALUES (?,?); '''
    cur = conn.cursor()
    cur.execute(sql, oc)
    conn.commit()


#Insert data into Session table
def insert_session(conn, session):
    sql = ''' Insert OR IGNORE into Session(SessionName,SessionType)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, session)
    conn.commit()

#Insert data into Staff table
def insert_staff(conn, staff):
    sql = ''' Insert OR IGNORE into Staff(TeachingCode,Name,Position)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, staff)
    conn.commit()

#Insert data into TeachingCode table
def insert_teachingcode(conn, TeachingCode):
    sql = ''' Insert OR IGNORE into TeachingCode(TeachingName)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, TeachingCode)
    conn.commit()

#Insert data into Unit table
def insert_unit(conn, unit):
    sql = ''' INSERT OR IGNORE INTO Unit(UnitName,UnitCode,Semester,Year)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, unit)
    conn.commit()
    return cur.lastrowid


# # check if a session is makring session or delivery section
# def check_session(SessionName):
#   if 'mark' in SessionName.lower():
#     return 'Marking'
#   else:
#     return 'Delivery'

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
  excel_file ="New Template v0.2.xlsx"
  unit_detail,teaching_team,delivery,marking,NSC = Configure.get_details(excel_file)


  UnitName = unit_detail.iloc[2,1]
  UnitCode =unit_detail.iloc[0,1]
  Semester=unit_detail.iloc[1,1]
  Year =unit_detail.iloc[4,1]
  max_staff = unit_detail.iloc[5,1]
  max_NSC = unit_detail.iloc[6,1]

  teachingcodes = teaching_team.iloc[2,1:max_staff+1]
  staffnames = teaching_team.iloc[0,1:max_staff+1]
  staffpositions = teaching_team.iloc[1,1:max_staff+1]
  staffrate = teaching_team.iloc[3,1:max_staff+1]


  payrates = teaching_team.iloc[3,1:max_staff+1]

  delivery_session =delivery.iloc[1:14,0]

  marking_session = marking.iloc[1:4,0]

  NSCNames = NSC.iloc[1:,0]
  NSCHours = NSC.iloc[1:,1]
  NSCRates = NSC.iloc[1:,2]
  NSCCost = NSC.iloc[1:,3]

  thisyear_detail = unit_detail.iloc[:,3]
  lastyear_detail = unit_detail.iloc[:,5]
  
  




  try:
    database = "Unit_Budget.db"

    #Create a database connection
    conn = create_connection(database)

    with conn:

      #Insert Unit table
      Unit = (UnitName,UnitCode,Semester,Year)
      UnitID = insert_unit(conn,Unit)

      #Insert TeachingCode table
      for TeachingName in teachingcodes:
        TeachingCode = [TeachingName]
        insert_teachingcode(conn,TeachingCode)


      #Insert Session table
      for SessionName in delivery_session:
        SessionType = 'Delivery'
        session = (SessionName,SessionType)
        insert_session(conn,session)

      for SessionName in marking_session:
        SessionType = 'Marking'
        session = (SessionName,SessionType)
        insert_session(conn,session)

      #insert into NonSalaryCost table and otherCost table

      for i in range(max_NSC):
        nonsalarycost = (NSCNames[i+1],NSCHours[i+1],NSCRates[i+1],NSCCost[i+1])
        nscid =insert_nsc(conn,nonsalarycost)
        oc = (nscid,UnitID)
        if oc !=0:
          insert_oc(conn,oc)

      #insert into budget table and enrolment table

      if check_numbers(thisyear_detail[1]):
        enrolment = (UnitID,thisyear_detail[1],'Yes','No')
        insert_enrolment(conn,enrolment)
      if check_numbers(thisyear_detail[3]):
        budget = (UnitID,thisyear_detail[3],'Yes','No')
        insert_budget(conn,budget)

      if check_numbers(lastyear_detail[1]):
        enrolment = (UnitID,lastyear_detail[1],'Yes','Yes')
        insert_enrolment(conn,enrolment)
      if check_numbers(lastyear_detail[2]):
        enrolment = (UnitID,lastyear_detail[2],'No','Yes')
        insert_enrolment(conn,enrolment)

      if check_numbers(lastyear_detail[3]):
        budget = (UnitID,lastyear_detail[3],'Yes','Yes')
        insert_budget(conn,budget)
      if check_numbers(lastyear_detail[4]):
        budget = (UnitID,lastyear_detail[4],'No','Yes')
        insert_budget(conn,budget)


      #insert into staff table

      for i in range(len(staffnames)):
        result = select_query(conn,'Select * from TeachingCode')
        for j in result:
          if j[1] == teachingcodes[i]:
            teachingid = j[0]
            break
        staff = (teachingid,staffnames[i],staffpositions[i])
        insert_staff(conn,staff)


      #insert into activities table


      for i in range(len(staffnames)):
        staffresult = select_query(conn,'Select StaffID,Name from Staff')
        for j in staffresult:
          if j[1] ==staffnames[i]:
            StaffID = j[0]
            break
        dsresult = select_query(conn,'Select SessionID, SessionName from Session')
        for k in range(len(delivery_session)):
          for a in dsresult:
            if a[1] == delivery_session[k+1]:
              SessionID = a[0]
              break
          if math.isnan(delivery.iloc[k+1,i+3]):
            continue
          else:
            activity = (UnitID, StaffID, SessionID, delivery.iloc[k+1,1], 0, payrates[i], delivery.iloc[k+1,i+3])
            insert_activities(conn,activity)

        for b in range(len(marking_session)):
          for c in dsresult:
            if c[1]  == marking_session[b+1]:
              SessionID = c[0]
              break
            if math.isnan(marking.iloc[b+1,i+3]):
              continue
            else:
              activity = (UnitID, StaffID, SessionID, 0, marking.iloc[b+1,2], payrates[i], marking.iloc[b+1,i+3])
              insert_activities(conn,activity)







        # activity = (UnitID, StaffID, SessionID, HourPerSession, MarkingHourPS, PayRate, Hour)
        # insert_activities(conn,activity)



        

        
        

      




    print("Dummy Unit data has been inserted")

  except Error as e:
    print(e)

if __name__ == '__main__':
  main()

