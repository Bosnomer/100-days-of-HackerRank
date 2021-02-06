# Weather Observation Station 17

SELECT ROUND(LONG_W, 4)
FROM station
WHERE LAT_N IN (SELECT MIN(LAT_N) FROM station WHERE  LAT_N>38.7780);
