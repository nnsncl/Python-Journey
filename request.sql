SELECT * FROM membres;
SELECT prenom, nom FROM membres;
SELECT email FROM membres;

SELECT prenom, nom FROM membres WHERE ville = 'New-York';
SELECT prenom, nom, ville FROM membres WHERE ville = 'New-York' OR ville = 'Los-Angeles';

SELECT prenom, nom FROM membres WHERE nom LIKE '%y';
SELECT prenom, nom FROM membres WHERE nom LIKE 'b%';

SELECT prenom, nom FROM membres WHERE nom LIKE '_____';
SELECT prenom, nom FROM membres WHERE nom LIKE '__s%';

SELECT prenom, nom FROM membres WHERE nom LIKE '__s%' AND ville = 'New-York';

SELECT prenom, nom FROM membres ORDER BY nom ASC;
SELECT prenom, nom FROM membres ORDER BY nom DESC;

SELECT prenom, nom FROM membres ORDER BY nom ASC, prenom DESC;
SELECT prenom, nom FROM membres ORDER BY nom DESC, prenom ASC;

SELECT DISTINCT ville FROM membres;
SELECT DISTINCT ville FROM membres ORDER BY ville;

SELECT ville FROM membres GROUP BY ville;
SELECT ville, COUNT(*) FROM membres GROUP BY ville;
SELECT ville, COUNT(*) AS population FROM membres GROUP BY ville;
 
SELECT prenom, nom FROM membres ORDER BY nom LIMIT 4;
SELECT prenom, nom FROM membres ORDER BY nom LIMIT 4,4;
SELECT prenom, nom FROM membres ORDER BY nom LIMIT 8,4;

SELECT prenom, nom, ville FROM membres WHERE ville = 'New-York' LIMIT 2;
SELECT prenom, nom, ville FROM membres ORDER BY RAND() LIMIT 2;

SELECT prenom, nom, naissance FROM membres WHERE YEAR(naissance) = 1977;
SELECT prenom, nom, naissance FROM membres WHERE MONTH(naissance) = 10;
SELECT prenom, nom, naissance FROM membres WHERE DAY(naissance) = 10;

SELECT prenom, nom, naissance FROM membres WHERE YEAR(naissance) >= 1977 AND YEAR(naissance) <= 1983;
SELECT prenom, nom, naissance FROM membres WHERE YEAR(naissance) BETWEEN 1977 AND 1983 ORDER BY naissance, nom;

SELECT MAX(gross) FROM films WHERE release_year BETWEEN 2000 AND 2012
SELECT AVG(duration) / 60.0 AS avg_duration_hours FROM films
SELECT MAX(release_year) - MIN(release_year) AS difference FROM films
SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead FROM people
SELECT (MAX(release_year) - MIN(release_year)) / 10.0 AS number_of_decades FROM films
SELECT prenom, nom, DATE_FORMAT(naissance, '%d-%m-%Y') AS naissancesFR FROM membres ORDER BY naissance;
SELECT title FROM films WHERE release_year IN(2000, 2012) ORDER BY release_year
SELECT * FROM films WHERE release_year != 2015 ORDER BY duration
SELECT title, gross FROM films WHERE title LIKE 'M%' ORDER BY title
SELECT imdb_score, film_id FROM reviews ORDER BY imdb_score DESC


INSERT INTO membres (nom, prenom, email) VALUES ('Dodo', 'Do', 'dodo@dodo.do');
INSERT INTO membres (nom, prenom, email)
    VALUES  ('Dido', 'Di', 'dido@dodo.di');
            ('Dudo', 'Du', 'dudo@dodo.du');

INSERT INTO membres
    VALUES (null,
            'Niki',
            'Nik',
            'niki@nik.niki',
            '25 rue de Niki',
            '10000',
            'Nikitown',
            '555-23456',
            '1994-10-10',
            NOW()
            );

INSERT INTO membres SET nom='coucou', prenom= 'Nik', ville='Nikitown', cp='10000'

UPDATE membres SET ville = 'Nikiland', cp='10001' -- Update every rows
UPDATE membres SET ville = 'Nikiland', cp='10001' WHERE id = 17 -- Update a single row
UPDATE membres SET ville = 'Nikiland', cp='10001' WHERE id IN (17, 18, 13, 8) -- Update multiple rows

UPDATE membres SET ville = 'Los Angeles' WHERE ville = 'Los-Angeles'

DELETE from membres --  Empty a table
DELETE from membres WHERE id = 19 -- delete a row


