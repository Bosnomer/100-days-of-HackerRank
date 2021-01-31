# African Cities

SELECT city.name
FROM city, country
WHERE continent="Africa" and city.countrycode=country.code;
