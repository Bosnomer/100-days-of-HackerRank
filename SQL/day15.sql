# Higher Than 75 Marks

SELECT name
FROM students
WHERE marks > 75
ORDER BY SUBSTRING(name, -3), id
