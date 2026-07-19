SELECT course, COUNT(*) AS total_students
FROM students
GROUP BY course;