# Weather Observation Station 20

SELECT ROUND(s.lat_n,4) FROM station s
WHERE (SELECT ROUND(COUNT(s.id)/2)-1 FROM station) = 
    (SELECT COUNT(s1.id) FROM station s1 
        WHERE s1.lat_n > s.lat_n);
