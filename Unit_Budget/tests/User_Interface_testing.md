# Deliverable 3

## How to start the automate testing for user_interface 

#### **Instruction**

<pre>

**In order to start the automate test, it requires to comment out mainWindow.webContents.openDevTools() in main.js, as this open development tools which could affect the testing**
https://github.com/WentworthJin/Unit_Budget_Planner/blob/master/Unit_Budget/main.js#L5 link to main.js

**For All User (automate testing front end)**

**Assume that user are in Unit_Budget_Planner directory**

cd Unit_Budget

npm run test:e2e

<pre>
Tests that I have created: 
opens a window
title
get the element name
click the roles
navigate to summary report
back to main page
comment button
input values for comment
check the clear function 
filter button 
check filter button and use the unit filter 
</pre>

</pre>

<hr>

## Result of the testing

<pre>

**For All User (automate testing front end)**

Application Launch
    ✔ opens a window
    ✔ title
    ✔ get the element name
    ✔ click the roles (1522ms)
    ✔ navigate to summary report (1516ms)
    ✔ back to the main page (1514ms)
    ✔ comment button (1518ms)
    ✔ input values for comment (1918ms)
    ✔ check the clear function (2416ms)
    ✔ filter button (1517ms)
    ✔ Check filter and use the unit filter (1917ms)


11 passing (1m)

</pre>

