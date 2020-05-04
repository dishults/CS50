--list the titles of all movies in which both Johnny Depp and Helena Bonham Carter starred
SELECT title FROM movies
JOIN stars ON stars.movie_id=movies.id
JOIN people ON people.id=stars.person_id
WHERE name = "Johnny Depp" OR name = "Helena Bonham Carter"
GROUP BY title
HAVING count(title) = 2