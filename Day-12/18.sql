SELECT employees.name, departments.dept_name, employees.salary
FROM employees
JOIN departments
ON employees.dept_id = departments.dept_id