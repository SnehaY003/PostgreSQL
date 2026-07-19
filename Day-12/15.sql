SELECT *
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id;