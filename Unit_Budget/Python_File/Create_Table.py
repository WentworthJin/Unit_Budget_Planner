import sqlite3
import sys
from sqlite3 import Error

'''
    Functionality: The Create_Table.py aims to create a database named: Unit_Budget.db at the current directory. 
    
    You can run this file by: 
        1. Execute the file directly, for example, run " python3 Create_Table.py " on terminal
        2. Import the function "Schema()" from this file, and execute that function 
            " import Create_Table
                     Create_Table.Schema()
            "
    Parameters: None
    
    Result: Create Unit_Budget.db at Current_Directory/Unit_Budget.db

    Testing: Refer to the " test_Create_Table.py " testing file, in order to test if the function can 
             correctly create the Unit_Budget.db.

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

# Create a table from the create_table_sql statement
# The create_table_sql variable can be customized
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as f:
        print(f)

def Schema():

    # The name of database
    database = "BudgetSample.db"

    FirstRun = True

    # This is the Database schema command lines

    sql_create_unit_table = """ CREATE TABLE IF NOT EXISTS Unit (
                                        UnitID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        UnitName VARCHAR (100),
                                        UnitCode VARCHAR (10),
                                        Semester VARCHAR (10),
                                        Year INT (4),
                                        Comment VARCHAR (300)
                                );"""

    sql_create_teachingcode_table = """ CREATE TABLE IF NOT EXISTS TeachingCode (
                                                TeachingCode INTEGER PRIMARY KEY AUTOINCREMENT,
                                                TeachingName VARCHAR (50) UNIQUE
                                        );"""
    
    sql_create_staff_table = """ CREATE TABLE IF NOT EXISTS Staff (
                                        StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        TeachingCode INT REFERENCES TeachingCode (TeachingCode) ON DELETE RESTRICT ON UPDATE CASCADE,
                                        Name VARCHAR (50),
                                        Position  VARCHAR (30),
                                        UNIQUE (Name, Position)ON CONFLICT FAIL
                                );"""

    sql_create_session_table = """ CREATE TABLE IF NOT EXISTS Session (
                                        SessionID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        SessionName VARCHAR (50) UNIQUE,
                                        SessionType VARCHAR (10) 
                                );"""

    sql_create_nonsalarycost_table = """ CREATE TABLE IF NOT EXISTS NonSalaryCosts (
                                                NSCID INTEGER PRIMARY KEY AUTOINCREMENT,
                                                NSCName VARCHAR (50),
                                                Hours REAL,
                                                CostPerHour REAL,
                                                TotalCost REAL,
                                                UNIQUE (NSCName, CostPerHour) ON CONFLICT FAIL
                                        );"""

    sql_create_othercost_table = """ CREATE TABLE IF NOT EXISTS OtherCost (
                                            OCID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            NSCID INT REFERENCES NonSalaryCosts (NSCID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                            UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                            Comment VARCHAR (300)
                                    );"""

    sql_create_enrollment_table = """ CREATE TABLE IF NOT EXISTS Enrolment (
                                            EnrolmentID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                            EnrolmentNumber INT,
                                            IsEstimated VARCHAR (3),
                                            IsLastSemester VARCHAR (3) 
                                    );"""

    sql_create_budget_table = """ CREATE TABLE IF NOT EXISTS Budget (
                                        BudgetID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                        Cost INT,
                                        IsEstimated VARCHAR (3),
                                        IsLastSemester VARCHAR (3) 
                                );"""

    sql_create_activities_table = """ CREATE TABLE IF NOT EXISTS Activities (
                                        ActivitiesID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                        StaffID INT REFERENCES Staff (StaffID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                        SessionID INT REFERENCES Session (SessionID) ON DELETE RESTRICT ON UPDATE CASCADE,
                                        HourPerSession INT,
                                        MarkingHourPS REAL,
                                        PayRate REAL,
                                        Hour REAL,
                                        Comment VARCHAR (300) 
                                    );"""
    sql_create_staff_view = ''' CREATE VIEW StaffDetail AS
                                    Select UnitName, UnitCode, Semester, Year, T1.Name AS Staff_Name, T1.Position AS Staff_Position, 
                                    (Select COUNT(T1.StaffID) AS Total_Sessions_Teached
                                    From Activities A5 JOIN Session S5 USING (SessionID)
                                                    JOIN Staff T5 USING (StaffID)
                                                    JOIN Unit U5 USING (UnitID)
                                                    JOIN TeachingCode P5 USING (TeachingCode)
                                    Where A5.StaffID = A1.StaffID
                                    Group By T5.StaffID) AS Number_of_Sessions_Teached
                                    ,A1.PayRate, 
                                    round((Select SUM(Hour) as NonMarking_Workload
                                    From Activities A2 JOIN Session S2 USING (SessionID)
                                                    JOIN Staff T2 USING (StaffID)
                                                    JOIN Unit U2 USING (UnitID)
                                                    JOIN TeachingCode P2 USING (TeachingCode)
                                    Where S2.SessionType = "NM" and A2.StaffID = A1.StaffID
                                    Group by T2.StaffID),0) AS NonMarking_Workload_Hour,
                                    round((Select SUM(Hour) as NonMarking_Workload
                                    From Activities A3 JOIN Session S3 USING (SessionID)
                                                    JOIN Staff T3 USING (StaffID)
                                                    JOIN Unit U3 USING (UnitID)
                                                    JOIN TeachingCode P3 USING (TeachingCode)
                                    Where S3.SessionType = "M" and A3.StaffID = A1.StaffID
                                    Group by T3.StaffID),0) AS Marking_Workload_Hour,
                                    round(SUM(Hour),0) as Total_WorkLoad_Hour, round(A1.PayRate*SUM(Hour),0) AS Total_Cost
                                    From Activities A1 JOIN Session S1 USING (SessionID)
                                                    JOIN Staff T1 USING (StaffID)
                                                    JOIN Unit U1 USING (UnitID)
                                                    JOIN TeachingCode P1 USING (TeachingCode)
                                    Group by T1.StaffID;'''

    sql_create_unit_view = '''CREATE VIEW UnitDetail AS
                                SELECT U.UnitCode, U.UnitName, U.Semester, U.Year, 
                                (SELECT COUNT(DISTINCT P.Name) FROM Activities A JOIN Staff P USING (StaffID) JOIN Unit R USING (UnitID) WHERE R.UnitCode = U.UnitCode) AS Staff_Number, 
                                (SELECT EnrolmentNumber FROM Enrolment JOIN Unit USING (UnitID) WHERE IsEstimated = "YES" and IsLastSemester = "NO" and Unit.UnitID = U.UnitID) AS Estimate_StudentNumber, 
                                round((SELECT SUM(N.TotalCost) FROM OtherCost O JOIN NonSalaryCosts N USING (NSCID) JOIN Unit Z USING (UnitID) WHERE Z.UnitID = U.UnitID GROUP BY Z.UnitID),0) AS Total_NonSalaryCost, 
                                round((SELECT SUM(A1.PayRate * Hour) AS Total_Cost FROM Activities A1 JOIN Session S1 USING (SessionID) JOIN Staff T1 USING (StaffID) JOIN Unit U1 USING (UnitID) JOIN TeachingCode P1 USING (TeachingCode) WHERE U1.UnitID = U.UnitID GROUP BY U1.UnitID),0) AS Total_SalaryCost, 
                                round((SELECT SUM(N.TotalCost) FROM OtherCost O JOIN NonSalaryCosts N USING (NSCID) JOIN Unit Z USING (UnitID) WHERE Z.UnitID = U.UnitID GROUP BY Z.UnitID) + (SELECT SUM(A1.PayRate * Hour) AS Total_Cost FROM Activities A1 JOIN Session S1 USING (SessionID) JOIN Staff T1 USING (StaffID) JOIN Unit U1 USING (UnitID) JOIN TeachingCode P1 USING (TeachingCode) WHERE U1.UnitID = U.UnitID GROUP BY U1.UnitID),0) AS Total_Cost, 
                                (SELECT B.Cost FROM Unit G JOIN Budget B USING (UnitID) WHERE IsEstimated = "YES" and B.IsLastSemester = "NO" and G.UnitID = U.UnitID) AS Estimate_Budget, (SELECT COUNT(DISTINCT (SessionID)) FROM Activities WHERE Activities.UnitID = U.UnitID GROUP BY UnitID) AS Number_of_Assigned_Seesion, 
                                (SELECT COUNT(*) FROM OtherCost O JOIN Unit L USING (UnitID) JOIN NonSalaryCosts USING (NSCID) WHERE L.UnitID = U.UnitID GROUP BY L.UnitID) AS Total_Number_of_NSC, 
                                round((SELECT SUM(A.Hour) FROM Activities A JOIN Unit N USING (UnitID) WHERE N.UnitID = U.UnitID GROUP BY N.UnitID),0) AS Total_Staff_WorkLoad 
                                FROM Activities A JOIN Staff S USING (StaffID) JOIN Session E USING (SessionID) JOIN Unit U USING (UnitID) 
                                GROUP BY U.UnitID;'''
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

        create_table(conn,sql_create_unit_view)

        create_table(conn,sql_create_staff_view)

        print("DB has been initialized")
    else:
        print("Error! Failed create the database connection.")
        print("Please try again")


if __name__ == '__main__':
    Schema()
