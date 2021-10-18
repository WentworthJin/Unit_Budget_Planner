# User Interface Related Testing

## How to start the test 

#### **Instruction**

<hr>

<pre>

**For All User (test back_end)**

**assuming that user venv virtual environment still activate**

assume that user are in Unit_Budget directory

cd Unit_Budget/Python_File

python3 testing_backend.py

</pre>

<pre>

**In order to start the automate test, it requires to comment out mainWindow.webContents.openDevTools() in main.js, as this open development tools which could affect the testing**
https://github.com/WentworthJin/Unit_Budget_Planner/blob/master/Unit_Budget/main.js#L5 link to main.js

**For All User (automate testing front end)**

assume that user are in Unit_Budget_Planner directory

cd Unit_Budget

npm run test:e2e

<pre>
Tests that I have created: 
opens a window
title
get the element name
navigate to summary report
</pre>

</pre>

<hr>

## Result of the testing

<pre>
**For All User (test back_end)**

DB has been initialized
test_all_data (__main__.FlaskTestCase) ... ok
test_back_button (__main__.FlaskTestCase) ... ok
test_employee_data (__main__.FlaskTestCase) ... ok
test_flask (__main__.FlaskTestCase) ... ok
test_summary_report (__main__.FlaskTestCase) ... ok
test_workload_data (__main__.FlaskTestCase) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.042s

OK

</pre>

<pre>

**For All User (automate testing front end)**

> electron-quick-start@1.0.0 test:e2e /Users/sameam/Desktop/OneDrive/Desktop/Professional/project1/Unit_Budget_Planner/Unit_Budget
> ./node_modules/mocha/bin/mocha tests/test.js  --timeout 30000



  Application Launch
    ✔ opens a window
    ✔ title
    ✔ get the element name
    ✔ navigate to summary report
    ✔ select role as Head of Finance (5033ms)


  5 passing (29s)

</pre>

