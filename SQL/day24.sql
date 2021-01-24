# The PADS 

SET @sumdoc  = (SELECT COUNT(*) FROM occupations WHERE occupation = "Doctor");
SET @sumsing  = (SELECT COUNT(*) FROM occupations WHERE occupation = "Singer");
SET @sumact  = (SELECT COUNT(*) FROM occupations WHERE occupation = "Actor");
SET @sumprof  = (SELECT COUNT(*) FROM occupations WHERE occupation = "Professor");

SELECT CONCAT(name, '','(', LEFT(occupation, 1),')') AS name
FROM occupations
ORDER BY name;

SELECT "There are a total of", @sumdoc,"doctors.";
SELECT "There are a total of", @sumact,"actors.";
SELECT "There are a total of", @sumsing,"singers.";
SELECT "There are a total of", @sumprof,"professors.";
