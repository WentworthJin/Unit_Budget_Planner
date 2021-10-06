# Unit Budget Planner Database User Guide

<hr><br>

## User Guide

- [DB Structure](#db_structure)
- [Tables](#tables)
  - [Activities](#activities)


<hr><br>

## DB_Structure
![image info](./Resources/DBStructure_V2.png)

<hr><br>

## Tables

### Activities

- Table Schema DDL

<pre>

CREATE TABLE IF NOT EXISTS Activities (
    ActivitiesID INT PRIMARY KEY,
    UnitID INT REFERENCES Unit (UnitID) ON DELETE RESTRICT ON UPDATE CASCADE,
    StaffID INT REFERENCES Staff (StaffID) ON DELETE RESTRICT ON UPDATE CASCADE,
    SessionID INT REFERENCES Session (SessionID) ON DELETE RESTRICT ON UPDATE CASCADE,
    HourPerSession INT,
    MarkingHourPS INT,
    Hour INT,
    Comment VARCHAR (300) 
);

</pre>
