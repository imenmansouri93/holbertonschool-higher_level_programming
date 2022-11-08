-- lists all cities contained in the database
SELECT cities.id, cities.name, states.name
FROM cities
WHERE join states ON cities.state_id = states.id