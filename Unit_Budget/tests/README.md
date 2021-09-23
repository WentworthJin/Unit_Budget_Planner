# Deliverable 2

## How to start the test 

#### **Instruction**

<hr>

<pre>

**For All User (test back_end)**

**assuming that user venv virtual environment still activate**

cd Unit_Budget/Python_File

python3 testing_backend.py

</pre>

<pre>

**For All User (automate testing front end)**

cd Unit_Budget

npm run test:e2e
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
> ./node_modules/mocha/bin/mocha tests/test.js  --timeout 10000



  Application Launch
    ✔ opens a window
    ✔ Navigate to Summary report (5061ms)


  2 passing (18s)

</pre>

