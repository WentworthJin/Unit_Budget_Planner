

INSERT INTO teaching_code (teaching_name) VALUES
('No Cost');
INSERT INTO teaching_code (teaching_name) VALUES
('ORAA(Hon Degree)');
INSERT INTO teaching_code (teaching_name) VALUES
('ORAA');
INSERT INTO teaching_code (teaching_name) VALUES
('ORAA(PHD)');
INSERT INTO teaching_code (teaching_name) VALUES
('Teaching Technician');
INSERT INTO teaching_code (teaching_name) VALUES
('Specialised Lecture');
INSERT INTO teaching_code (teaching_name) VALUES
('Developed Lecture');



INSERT INTO staff (teaching_id,name,position) VALUES
(1,'Lyndon While','Academic staff');
INSERT INTO staff (teaching_id,name,position) VALUES
(2,'Manou Rosenberg','Casual teaching');
INSERT INTO staff (teaching_id,name,position) VALUES
(3,'Casual 2','Casual teaching');



INSERT INTO section(section_name,type) VALUES
('Lecture','Delivery');
INSERT INTO section(section_name,type) VALUES
('F2F workshop','Delivery');
INSERT INTO section(section_name,type) VALUES
('Online workshop','Delivery');
INSERT INTO section(section_name,type) VALUES
('Laboratory','Delivery');
INSERT INTO section(section_name,type) VALUES
('Project 1 Marking','Marking');
INSERT INTO section(section_name,type) VALUES
('Project 2 Marking','Marking');
INSERT INTO section(section_name,type) VALUES
('Exam Marking','Marking');


INSERT INTO unit(unit_code,year,semester,actual_enrolment,estimated_enrolment,actual_budget,estimated_budget) VALUES
('CITS1101',2021,2,0,410,0,34286);

insert into non_salary_cost(unit_id,NSC_name,cost) VALUES
(1,"marking mid-semester test",400);

insert into activity(unit_id,section_id,staff_id,hour,cost) values
(1,2,2,112,6492);
insert into activity(unit_id,section_id,staff_id,hour,cost) values
(1,3,3,112,6102);
insert into activity(unit_id,section_id,staff_id,hour,cost) values
(1,4,3,112,6103);
insert into activity(unit_id,section_id,staff_id,hour,cost) values
(1,5,3,93,5062);



