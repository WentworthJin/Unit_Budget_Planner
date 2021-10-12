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
    database = "Unit_Budget.db"

    FirstRun = True

    # This is the Database schema command lines

    sql_create_unit_table = """ CREATE TABLE Unit (
                                        UnitID   INTEGER       PRIMARY KEY AUTOINCREMENT,
                                        UnitName VARCHAR (100),
                                        UnitCode VARCHAR (10),
                                        Semester VARCHAR (10),
                                        Year     INT (4),
                                        Comment  VARCHAR (300) DEFAULT NoRecord
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

    sql_create_nonsalarycost_table = """ CREATE TABLE NonSalaryCosts (
                                                NSCID       INTEGER      PRIMARY KEY AUTOINCREMENT,
                                                NSCName     VARCHAR (50),
                                                Hours       REAL,
                                                CostPerHour REAL,
                                                TotalCost   REAL         DEFAULT (0),
                                                UNIQUE (
                                                    NSCName,
                                                    Hours,
                                                    CostPerHour
                                                )
                                                ON CONFLICT FAIL
                                        );"""

    sql_create_othercost_table = """ CREATE TABLE OtherCost (
                                            OCID    INTEGER       PRIMARY KEY AUTOINCREMENT,
                                            NSCID   INT           REFERENCES NonSalaryCosts (NSCID) ON DELETE RESTRICT
                                                                                                    ON UPDATE CASCADE,
                                            UnitID  INT           REFERENCES Unit (UnitID) ON DELETE RESTRICT
                                                                                        ON UPDATE CASCADE,
                                            Comment VARCHAR (300) DEFAULT NoRecord
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

    sql_create_activities_table = """ CREATE TABLE Activities (
                                            ActivitiesID   INTEGER       PRIMARY KEY AUTOINCREMENT,
                                            UnitID         INT           REFERENCES Unit (UnitID) ON DELETE RESTRICT
                                                                                                ON UPDATE CASCADE,
                                            StaffID        INT           REFERENCES Staff (StaffID) ON DELETE RESTRICT
                                                                                                    ON UPDATE CASCADE,
                                            SessionID      INT           REFERENCES Session (SessionID) ON DELETE RESTRICT
                                                                                                        ON UPDATE CASCADE,
                                            HourPerSession INT,
                                            MarkingHourPS  REAL,
                                            PayRate        REAL,
                                            Hour           REAL,
                                            Comment        VARCHAR (300) DEFAULT NoRecord
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
    Schema()
