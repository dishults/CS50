--list the names of all people who starred in a movie released in 2004, ordered by birth year
SELECT name FROM people
JOIN stars ON stars.movie_id=people.id
JOIN movies ON movies.id=stars.movie_id
WHERE year=2004
GROUP BY name
ORDER BY birth