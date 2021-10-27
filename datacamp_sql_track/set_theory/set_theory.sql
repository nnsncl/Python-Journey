-- Select fields from 2010 table
SELECT *
  -- From 2010 table
  FROM economies2010
	-- Set theory clause
	UNION
-- Select fields from 2015 table
SELECT *
  -- From 2015 table
  FROm economies2015
-- Order by code and year
ORDER BY code, year;

-- Select field
SELECT country_code
  -- From cities
  FROM cities
	-- Set theory clause
	UNION
-- Select field
SELECT code
  -- From currencies
  FROM currencies
-- Order by country_code
ORDER BY country_code;

-- Select fields
SELECT code, year
  -- From economies
  FROM economies
	-- Set theory clause
	UNION ALL
-- Select fields
SELECT country_code, year
  -- From populations
  FROM populations
-- Order by code, year
ORDER BY code, year;

-- Select fields
SELECT code, year
  -- From economies
  FROm economies
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT country_code, year
  -- From populations
  FROM populations
-- Order by code and year
ORDER BY code, year;

-- Select fields
SELECT code, name
  -- From countries
  FROM countries
	-- Set theory clause
	INTERSECT
-- Select fields
SELECT country_code, name
  -- From cities
  FROM cities;

  -- Select field
SELECT name
  -- From cities
  FROM cities
	-- Set theory clause
	EXCEPT
-- Select field
SELECT capital
  -- From countries
  FROM countries
-- Order by result
ORDER BY name;

-- Select field
SELECT capital
  -- From countries
  FROM countries
	-- Set theory clause
	EXCEPT
-- Select field
SELECT name
  -- From cities
  FROM cities
-- Order by ascending capital
ORDER BY capital;

-- Select code
SELECT code 
  -- From countries
  FROM countries
-- Where region is Middle East
WHERE region = 'Middle East';

-- Query from step 2
SELECT DISTINCT name
  FROM languages
-- Where in statement
WHERE code IN 
  -- Query from step 1
  -- Subquery
  (SELECT code
   FROM countries
   WHERE region = 'Middle East')
-- Order by name
ORDER BY name;


-- Select statement
SELECT COUNT(*)
  -- From countries
  FROM countries
-- Where continent is Oceania
WHERE continent = 'Oceania';

-- Select fields (with aliases)
SELECT c1.code, c1.name, c2.basic_unit AS currency
  -- From countries (alias as c1)
  FROM countries AS c1
  	-- Join with currencies (alias as c2)
  	INNER JOIN currencies AS c2
    -- Match on code
    ON c1.code = c2.code
-- Where continent is Oceania
WHERE continent = 'Oceania';

-- Select fields
SELECT code, name
  -- From Countries
  FROM countries
  -- Where continent is Oceania
  WHERE continent = 'Oceania'
  	-- And code not in
  	AND code NOT IN
  	-- Subquery
  	(SELECT code FROM currencies);