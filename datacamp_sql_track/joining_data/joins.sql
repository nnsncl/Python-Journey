SELECT * 
FROM cities
  -- Inner join to countries
  INNER JOIN countries
    -- Match on the country codes
    ON cities.country_code = countries.code;


-- Select name fields (with alias) and region 
SELECT cities.name AS city, countries.name AS country, region
FROM cities
  INNER JOIN countries
    ON cities.country_code = countries.code;


-- Select fields with aliases
SELECT c.code AS country_code, name, year, inflation_rate
FROM countries AS c
  -- Join to economies (alias e)
  INNER JOIN economies AS e
    -- Match on code
    ON c.code = e.code;


-- Select fields
SELECT code, name, region, year, fertility_rate
  -- From countries (alias as c)
  FROM countries AS c
  -- Join with populations (as p)
  INNER JOIN populations AS p
    -- Match on country code
    ON c.code = p.country_code;


-- Select fields
SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
  -- From countries (alias as c)
  FROM countries AS c
  -- Join to populations (as p)
  INNER JOIN populations AS p
    -- Match on country code
    ON c.code = p.country_code
  -- Join to economies (as e)
  INNER JOIN economies AS e
    -- Match on country code and year
    ON c.code = e.code AND e.year = p.year;


-- Select fields
SELECT c.name as country, continent, l.name AS language, official
  -- From countries (alias as c)
  FROM countries AS c
  -- Join to languages (as l)
  INNER JOIN languages AS l
    -- Match using code
    USING (code)


-- Select fields with aliases
SELECT p1.country_code,
       p1.size AS size2010, 
       p2.size AS size2015,
       -- Calculate growth_perc
       ((p2.size - p1.size)/p1.size * 100.0) AS growth_perc
-- From populations (alias as p1)
FROM populations AS p1
  -- Join to itself (alias as p2)
  INNER JOIN populations AS p2
    -- Match on country code
    ON p1.country_code = p2.country_code
        -- and year (with calculation)
        AND p1.year = p2.year - 5;



SELECT name, continent, code, surface_area,
    -- First case
    CASE WHEN surface_area > 2000000 THEN 'large'
        -- Second case
        WHEN surface_area > 350000 THEN 'medium'
        -- Else clause + end
        ELSE 'small' END
        -- Alias name
        AS geosize_group
-- From table
FROM countries;


SELECT country_code, size,
    -- First case
    CASE WHEN size > 50000000 THEN 'large'
        -- Second case
        WHEN size > 1000000 THEN 'medium'
        -- Else clause + end
        ELSE 'small' END
        -- Alias name (popsize_group)
        AS popsize_group
-- From table
INTO pop_plus       
FROM populations
WHERE year = 2015;

-- Select fields
SELECT name, continent, geosize_group, popsize_group
-- From countries_plus (alias as c)
FROM countries_plus AS c
  -- Join to pop_plus (alias as p)
  INNER JOIN pop_plus as p
    -- Match on country code
    ON c.code = p.country_code
-- Order the table    
 ORDER BY geosize_group ASC;