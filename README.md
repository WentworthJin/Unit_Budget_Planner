# Deliverable 2

<b>Why this branch<b>

This branch concentrates on the implementation of the feature of filtering summary reports. However, in order to avoid potential conflicts, master branch may merge into this branch when needed. 

<b>What is this feature?<b>

Users can choose options (Year, Semester, Unit Code) on the menu filter, which makes the users can see specific information such as budget for semester 1 2020 budget for specific unit. 

<b>How to use this feature ?<b>

step 1:  refer to How to Lauche the Application

step 2:  click the "Summary Report" button.

step 3:  you can see the dropdown box to choose the year and the semester and the edit box to input the unit code. Make some change on the three fields and you can see the different information and bar charts. For example, if you choose 2020, you can only see the information about 2020. If you input CITS5503 in the edit box, you can only see the information about CITS5503.


## How to Launch the Application

**In order to use the interface, will require to install node.js at https://nodejs.org/en/download/**

You need to install the packages inside the [<b>requirements.txt<b>](./Unit_Budget/Python_File/requirements.txt). Run the following codes.
<pre>

**Install virtual Environment**

cd Unit_Budget

python3 -m venv venv 

source venv/bin/activate

pip3 install -r ./Unit_Budget/Python_File/requirements.txt

npm install

npm start

</pre>

<hr>

