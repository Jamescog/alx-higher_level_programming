-- create the MySQL server user user_0d_1.
-- the user_0d_1 will be set user_0d_1_pwd
-- if the user_0d_1 exists it will not fail
CREATE USER
	IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
	ON *.*
	TO 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
