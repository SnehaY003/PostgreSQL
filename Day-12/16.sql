SELECT * FROM students
LEFT JOIN courses
ON students.course = courses.course_name;