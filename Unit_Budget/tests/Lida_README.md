
## How to start the test 

### **Instruction**

<hr>

<pre>
As most of the tests have been done by the other project team member, I have created two tests, one is an automate testing, another one is a manual testing. 

**In order to start the automate testing, it requires to comment out mainWindow.webContents.openDevTools() in main.js, as this open development tools which could affect the testing**
https://github.com/WentworthJin/Unit_Budget_Planner/blob/master/Unit_Budget/main.js#L5 link to main.js

**For All Users (automate testing front end)**

Assume that user are in Unit_Budget_Planner directory

cd Unit_Budget

npm run test:e2e

<pre>
Automate testing that I have created: 
- select role as Head of Finance

This test is testing the role selection button, when click, there should be a display underneath with "You are the Head of Finance.". Same functionality for all the other roles. This functionality will be future modified to show different home page, e.g., Head of Department will be able to bulk upload.
</pre>

</pre>

<hr>

## Result of the automate testing

<pre>

**For All Users (automate testing front end)**

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

<pre>

Due to the time limitation, the following testing has not been setup as an automate testing. 

Manual testing that I have created: 
upload unit budget spreadsheet to the system

This test is testing the "Upload" button, when click without "Choose file", i.e. the display is "No file chosen", the "Upload" button will not be redirect to the table.html. 

Manual test steps: 
1. Start the application (refer to README.md at Unit_Budget_Planner/README.md)
2. Download the unit budget spreadsheet at https://github.com/WentworthJin/Unit_Budget_Planner/raw/master/Unit_Budget/tests/CITS4401_Sem1%202021%20budgetv3.xlsx
2. Click "Choose file" and select the "CITS4401_Sem1 2021 budgetv3"
3. Click the "Upload" button

</pre>

<hr>

## Result of the testing

<pre>

**For All Users (manual testing front end)**

It will be redirect to the table.html. 

This functionality will be further improved to only accept spreadsheet files, automatically store the data in the database and extract the database result and display in the tables. 

</pre>


