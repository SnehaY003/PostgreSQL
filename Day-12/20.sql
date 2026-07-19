SELECT employees.name, departments.dept_name
FROM employees
JOIN departments
ON employees.employee_id = departments.dept_id
WHERE departments.dept_name = 'HR';