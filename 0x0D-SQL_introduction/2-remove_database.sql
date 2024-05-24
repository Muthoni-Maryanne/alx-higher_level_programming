-- script that deletes the database hbtn_0c_0 in your MySQL server
-- If the database hbtn_0c_0 doesn’t exist, your script should not fail
-- Not allowed to use the SELECT or SHOW statements
-- check if present or not with cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
-- Execute drop with cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
DROP DATABASE IF EXISTS hbtn_0c_0;
