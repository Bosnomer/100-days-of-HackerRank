# Weather Observation Station 13

SELECT ROUND(SUM(LAT_N),4)
FROM station
WHERE LAT_N>38.7880 and LAT_N<137.2345;
