-- creates a table called first_table
-- Description: id INT, name VARCHAR(256)
-- If the table first_table already exists, your script should not fail
-- Not allowed to use the SELECT or SHOW statements
-- Execute with cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
-- List all tables with cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 after
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
