
INSERT INTO groups (group_name, faculty)
VALUES
('CS-101', 'Computer Science'),
('MATH-202', 'Mathematics');

INSERT INTO students (first_name, last_name, group_id)
VALUES
('Alice', 'Johnson', 1),
('Bob', 'Smith', 1),
('Charlie', 'Brown', 2),
('Diana', 'White', 2);

INSERT INTO grades (student_id, subject, grade, date)
VALUES
(1, 'Programming', 95, '2025-10-20'),
(2, 'Programming', 88, '2025-10-20'),
(3, 'Calculus', 76, '2025-10-20'),
(4, 'Linear Algebra', 89, '2025-10-20'),
(1, 'Databases', 91, '2025-10-21'),
(2, 'Databases', 85, '2025-10-21'),
(3, 'Mathematical Logic', 82, '2025-10-21');
