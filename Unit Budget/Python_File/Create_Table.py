import sqlite3
import sys
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

#Create a table from the create_table_sql statement
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as f:
        print(f)

#Insert data into Unit table
def create_unit(conn, unit):
    sql = ''' INSERT INTO Unit(UnitID,UnitCode,Semester,Year)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, unit)
    conn.commit()
    return cur.lastrowid


def main():
    database = "./DataBase/Unit_Budget.db"

    FirstRun = True

    sql_create_unit_table = """ CREATE TABLE IF NOT EXISTS Unit (
                                      UnitID INT PRIMARY KEY,
                                      UnitCode VARCHAR (10),
                                      Semester INT (1),
                                      Year INT (4) 
                                );"""

    sql_create_teachingcode_table = """ CREATE TABLE IF NOT EXISTS TeachingCode (
                                              TeachingCode INT PRIMARY KEY,
                                              TeachingName VARCHAR (50)
                                        );"""
    
    sql_create_staff_table = """ CREATE TABLE IF NOT EXISTS Staff (
                                      StaffID INT PRIMARY KEY,
                                      TeachingID INT REFERENCES TeachingCode (TeachingCode) ON DELETE RESTRICT ON UPDATE CASCADE,
                                      Name VARCHAR (50),
                                      Position  VARCHAR (30),
                                      UNIQUE (
                                                Name,
                                                Position
                                      )
                                      ON CONFLICT FAIL
                                  );"""

    sql_create_session_table = """ CREATE TABLE IF NOT EXISTS Session (
                                        SessionID INT PRIMARY KEY,
                                        SessionName VARCHAR (50) UNIQUE,
                                        SessionType VARCHAR (10) 
                                  );"""

    sql_create_nonsalarycost_table = """ CREATE TABLE IF NOT EXISTS NonSalaryCosts (
                                              NSCID PRIMARY KEY,
                                              NSCName VARCHAR (50),
                                              Hours INT,
                                              CostPerHour INT,
                                              TotalCost INT,
                                              UNIQUE (
                                                        NSCName,
                                                        CostPerHour
                                                      )
                                                ON CONFLICT FAIL
                                          );"""

    sql_create_othercost_table = """ CREATE TABLE IF NOT EXISTS OtherCost (
                                          OCID PRIMARY KEY,
                                          NSCID INT REFERENCES NonSalaryCosts (NSCID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                          UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE
                                      );"""

    sql_create_enrollment_table = """ CREATE TABLE IF NOT EXISTS Enrolment (
                                            EnrolmentID INT PRIMARY KEY,
                                            UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                            EnrolmentNumber INT,
                                            IsEstimated VARCHAR (3),
                                            IsLastSemester VARCHAR (3) 
                                      );"""

    sql_create_budget_table = """ CREATE TABLE IF NOT EXISTS Budget (
                                        BudgetID INT PRIMARY KEY,
                                        UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                        Cost INT,
                                        IsEstimated VARCHAR (3),
                                        IsLastSemester VARCHAR (3) 
                                  );"""

    sql_create_activities_table = """ CREATE TABLE IF NOT EXISTS Activities (
                                            ActivitiesID INT PRIMARY KEY,
                                            UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                            StaffID INT REFERENCES Staff (StaffID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                            SessionID  INT REFERENCES Session (SessionID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                            HourlyRate NUMERIC,
                                            Hour INT
                                      );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:

        create_table(conn, sql_create_unit_table)

        create_table(conn, sql_create_teachingcode_table)

        create_table(conn, sql_create_staff_table)

        create_table(conn, sql_create_session_table)

        create_table(conn,sql_create_nonsalarycost_table)

        create_table(conn,sql_create_othercost_table)

        create_table(conn,sql_create_enrollment_table)

        create_table(conn,sql_create_budget_table)

        create_table(conn,sql_create_activities_table)

        print("DB has been initialized")
    else:
        print("Error! Failed create the database connection.")
        print("Please try again")


if __name__ == '__main__':
    main()
