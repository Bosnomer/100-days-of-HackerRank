# Weather Observation Station 15

SET @v1 = (SELECT MAX(LAT_N) FROM station WHERE LAT_N<137.2345);

SELECT ROUND(LONG_W,4)
FROM station
WHERE LAT_N=@v1;
