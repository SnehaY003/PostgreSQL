CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) UNIQUE,
    duration VARCHAR(50),
    fees INT
);