-- list all records of the table second_table of database
-- start with top score on top
SELECT 
	`score`, `name`
FROM
	`first_table`
ORDER BY
	`score` DESC;
