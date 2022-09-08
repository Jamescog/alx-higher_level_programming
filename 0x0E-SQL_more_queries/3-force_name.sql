-- creates the table force_name on my MySQL server
-- if the table exists it won't fail
CREATE TABLE 
	IF NOT EXISTS 'force_name'
		(id INT,
		name VARCHAR(256));
