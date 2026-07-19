ALTER TABLE employees
ADD COLUMN dept_id INT;
ALTER TABLE employees
ADD CONSTRAINT f_dept
FOREIGN KEY(dept_id)
REFERENCES departments(dept_id);

UPDATE employees SET dept_id = 1 WHERE employee_id = 1;
UPDATE employees SET dept_id = 2 WHERE employee_id = 2;
UPDATE employees SET dept_id = 3 WHERE employee_id = 3;
UPDATE employees SET dept_id = 4 WHERE employee_id = 4;
UPDATE employees SET dept_id = 5 WHERE employee_id = 5;