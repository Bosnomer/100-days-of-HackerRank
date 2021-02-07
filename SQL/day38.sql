# Average Population of Each Continent

SELECT country.continent, FLOOR(AVG(city.population))
FROM country, city
WHERE country.code = city.countrycode
GROUP BY country.continent;
