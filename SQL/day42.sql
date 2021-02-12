# Top Earners

SELECT (salary * months) AS earnings ,COUNT(*) 
FROM employee 
GROUP BY 1 
ORDER BY earnings DESC 
LIMIT 1;
