# Weather Observation Station 5

SET @small = (SELECT MIN(LENGTH(city)) FROM station);
SET @big = (SELECT MAX(LENGTH(city)) FROM station);

SELECT city, LENGTH(city)
FROM station
WHERE LENGTH(city)=@small
ORDER BY city
LIMIT 1;

SELECT city, LENGTH(city)
FROM station
WHERE LENGTH(city)=@big
ORDER BY city
LIMIT 1;
