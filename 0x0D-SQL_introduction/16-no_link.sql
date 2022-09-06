-- list all records of the table second_tablse
-- it won't list rows without a name value
-- the record will be displayed by descenging score
SELECT
	score,
	name
FROM
	second_table
WHERE
	name NOT NULL
ORDER BY
	score DESC;
