-- Cities of CA
-- select cities where state_id corresponds to name "California"
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California");
