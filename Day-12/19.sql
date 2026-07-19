SELECT students.name, students.course, courses.duration, courses.fees
FROM students
LEFT JOIN courses
ON students.course = courses.course_name;
