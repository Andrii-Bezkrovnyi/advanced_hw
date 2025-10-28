SELECT last_name, first_name
FROM students s
INNER JOIN groups g ON s.group_id = g.group_id
WHERE group_name = 'CS-101';

SELECT
    s.student_id AS id,
    s.first_name,
    s.last_name,
    AVG(g.grade) AS average_grade
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
WHERE s.student_id = 1
GROUP BY s.student_id;

-- Вибрати назви всіх груп на факультеті 'Computer Science', в яких навчається більше 1 студентa.
SELECT
    g.group_name,
    g.faculty,
    COUNT(s.student_id) AS student_count
FROM groups g
JOIN students s ON g.group_id = s.group_id
WHERE g.faculty = 'Computer Science'
GROUP BY g.group_id
HAVING COUNT(s.student_id) > 1;

--Отримати прізвище студента та його найвищу оцінку з предмета 'Programming'.
SELECT
    s.last_name,
    MAX(g.grade) AS highest_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE g.subject = 'Programming'
GROUP BY s.student_id;

-- Вибрати прізвища та імена студентів, які не мають жодної оцінки в таблиці grades.
SELECT
    s.first_name,
    s.last_name
FROM students s
LEFT JOIN grades g ON s.student_id = g.student_id
WHERE g.grade IS NULL;

-- додати нового студента
INSERT INTO students (first_name, last_name, group_id)
VALUES ('Eve', 'Green', 1);

-- оновити назву групи з id 1 -> 'CS-101' на 'CS-103'
UPDATE groups
SET group_name = 'CS-103'
WHERE group_id = 1;

-- видалити всі оцінки, які були поставлені до 20 жовтня 2025 року і є нижчими за 60
DELETE FROM grades
WHERE date < '2025-10-20' AND grade < 60;


