# Weather Observation Station 16

SELECT ROUND(MIN(Lat_N), 4)
FROM station
WHERE lat_n > 38.7780;
