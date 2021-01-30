# Asian Population

SELECT SUM(city.population)
FROM city, country
WHERE continent = "Asia" and city.countrycode=country.code;
