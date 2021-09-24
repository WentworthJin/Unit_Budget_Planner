# Unit Budget Planning Project Individual Part

## Student:
- Liangbo Jin 23078811

<br><hr><br>

## 1. Create Table Function

### I. Functionality
- The [<b>Create_Table.py<b>](./Python_File/Create_Table.py) aims to create a database named: Unit_Budget.db at the current directory.

### II. How to run this code
- You can execute this file directly in the terminal( *Presuming you are in the [<b>Python_File<b>](./Python_File) directory)
  
  <pre>
  python3 Create_Table.py
  </pre>

### III. Resut
- You will get the 'Unit_Budget.db' created at the currect directory
  
  <pre>
  ***
  DB has been initialized
  ***
  
  Python_File
  |-- Create_Table.py
  |-- Unit_Budget.db --> *New created
  </pre>

### IV. Testing
- There is a [<b>testing<b>](./Python_File/test_Create_Table.py) file available for this functionality. 
- This file will test whether the function can successfully create the database name 'Unit_Budget.db'
- To run the testing file, you need to be in the [<b>Python_File<b>](./Python_File) directory
  
  <pre>
  python3 -m test_Create_Table
  </pre>
  
  And the testing result should be
  
  <pre>
  incomplete input
  .DB has been initialized
  .
  ----------------------------------------------------------------------
  Ran 2 tests in 0.010s

  OK
  </pre>

<br><hr><br>

## 2. Data Insertion function

### I. Functionality
- The [<b>Insert_All_Liangbo_Version.py.py<b>](./Python_File/Insert_All_Liangbo_Version.py) is a framework that provides various functions for other users to use, in
order to insert data into the database.

### II. How to run this code
- The file comes with mock data, so that you can execute this file directly in the terminal ( *Presuming you are in the [<b>Python_File<b>](./Python_File) directory)

- The mock data can be viewed [<b>here<b>](./Python_File/Insert_All_Liangbo_Version.py#L5-L13)
  
  <pre>
  python3 Create_Table.py
  python3 Insert_All_Liangbo_Version.py
  </pre>

### III. Resut
- You will be notified that all data has been inserted
  
  <pre>
  ***
  All Dummy data has been inserted
  ***
  </pre>

### IV. Testing
- There is a [<b>testing<b>](./Python_File/test_Insert_All.py) file available for this functionality. 
- This file will test whether the function can successfully load the mock data into the database 'Unit_Budget.db'
- To run the testing file, you need to be in the [<b>Python_File<b>](./Python_File) directory
  
  <pre>
  python3 -m test_Insert_All
  </pre>
  
  And the testing result should be
  
  <pre>
  DB has been initialized
  .........
  ----------------------------------------------------------------------
  Ran 9 tests in 0.009s

  OK
  </pre>

<br><hr><br>

## 3. Table Attribute Selection function

### I. Functionality
- The [<b>getFuction.py<b>](./Python_File/getFunction.py) is also a framework that provides some functions for other users to use, and enable them to get the 
primary key of Staff, TeachingCode, and Non-Salary Cost table.

### II. How to run this code
- In order to run this file, you need to run previous two function in order to make the mock data available in the database

- The file comes with one mock data, which will return the primary key for the one staff, so that you can execute this file directly in the terminal 
( *Presuming you are in the [<b>Python_File<b>](./Python_File) directory)

- The mock data can be viewed [<b>here<b>](./Python_File/getFunction.py#L66)
  
  <pre>
  python3 Create_Table.py
  python3 Insert_All_Liangbo_Version.py
  python3 getFunction.py
  </pre>

### III. Resut
- You will get the primary Key for that mock staff
  
  <pre>
  ***
  1
  ***
  </pre>

### IV. Testing
- There is a [<b>testing<b>](./Python_File/test_getID.py) file available for this functionality. 
- This file will test whether the function can successfully return the primary key regarding to the input
- To run the testing file, you need to be in the [<b>Python_File<b>](./Python_File) directory
  
  <pre>
  python3 -m test_getID
  </pre>
  
  And the testing result should be
  
  <pre>
  DB has been initialized
  All Dummy data has been inserted
  ...
  ----------------------------------------------------------------------
  Ran 3 tests in 0.001s

  OK
  </pre>
  
  <b><hr><b>
  
## 4. File Upload function

### I. Functionality
- The [<b>upload function<b>](./Python_File/route.py#L173-L189) is button, that when user upload a file and clicked this button, the functions inside will save 
the uploaded file into the directory [<b>uploads<b>(./Python_File/uploads) 

### II. How to run this code
- This functionality is embeded in the main project, therefore, you need to start the whole program to use this function

- The instructions can be viewed [<b>Here<b>](../README.md#L5-L45)

### III. Testing
- You can check if the file appeared in the [<b>uploads<b>](./Python_File/uploads) folder

