-- script that creates the table id_not_null on your MySQL server
-- id_not_null description: id INT with the default value 1, name VARCHAR(256)
-- If the table id_not_null already exists, your script should not fail
-- Execute with cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
CREATE TABLE
	IF NOT EXISTS id_not_null(
		id INT DEFAULT 1 NOT NULL,
		name VARCHAR(256));
