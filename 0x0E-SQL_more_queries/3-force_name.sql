-- script that creates the table force_name on your MySQL server
-- force_name description: id INT, name VARCHAR(256) can’t be null
-- If the table force_name already exists, your script should not fail
-- Execute with cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
CREATE TABLE
	IF NOT EXISTS force_name(
		id INT,
		name VARCHAR(256) NOT NULL)
