
-- Create 'groups' table
CREATE TABLE groups (
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL,
    faculty TEXT NOT NULL
);

-- Create 'students' table
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(group_id)
);

-- Create 'grades' table
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    grade REAL CHECK(grade >= 0 AND grade <= 100),
    date TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
