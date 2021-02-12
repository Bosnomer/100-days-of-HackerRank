# New Companies

SELECT c.company_code, c.founder,
    COUNT(DISTINCT lm.lead_manager_code), 
    COUNT(DISTINCT sm.senior_manager_code), 
    COUNT(DISTINCT m.manager_code), 
    COUNT(DISTINCT emp.employee_code) 
FROM Employee emp, Manager m, Senior_Manager sm, Lead_Manager lm , Company c
WHERE emp.company_code = m.company_code AND m.company_code = sm.company_code 
    AND sm.company_code = lm.company_code AND lm.company_code = c.company_code
GROUP BY c.company_code, c.founder 
ORDER BY c.company_code;
