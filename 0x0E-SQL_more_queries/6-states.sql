-- script that creates the database hbtn_0d_usa
-- the table states (in the database hbtn_0d_usa)
-- states description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail
-- Executed with cat 6-states.sql | mysql -hlocalhost -uroot -p
CREATE DATABASE
	IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE 
	IF NOT EXISTS states(
		id INT PRIMARY KEY UNIQUE AUTO_INCREMENT,
		name VARCHAR(256) NOT NULL);
