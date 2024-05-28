# 0x0E. SQL - More queries
This is a continuation of SQL.
## Resources
1. [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
2. [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
3. [MySQL constraints](https://zetcode.com/mysql/constraints/)
4. [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
5. [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
6. [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
7. [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
8. [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
9. [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
10. [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
11. [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
12. [SQL Style Guide](https://www.sqlstyle.guide/)
13. [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
14. [Design](https://www.guru99.com/database-design.html)
15. [Normalization](https://www.guru99.com/database-normalization.html)
16. [ER modelling](https://www.guru99.com/er-modeling.html)
## Summary
**Create a New User and Grant Permissions in MySQL**
1. Log into MySQL server: ```$ sudo mysql``` if using auth_socket or ```$ sudo -u root -p``` if using password
2. Create user: ```$ CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';``` to create a user that authenticates with auth_socket or ```$ CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';``` to create a user that authenticates with caching_sha2_password.
3. Grant permission. Syntax: ```GRANT PRIVILEGE ON database.table TO 'username'@'host';```
   Example- ```GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;```
   Example to grant all permissions globally: ```GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;```

4. Flush privileges to to reload the grant tables to ensure that the new privileges are put into effect:```FLUSH PRIVILEGES;```
5. Exit: ```exit```
6. Log in in future: ```mysql -u sammy -p```

Note:
- To revoke permissions: ```REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';```
- Review a user’s current permissions: ```SHOW GRANTS FOR 'username'@'host';```
- Delete a user: ```DROP USER 'username'@'localhost';```

**MySQL GRANT**

![Screenshot 2024-05-24 161142](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/5bc82f74-551a-461e-8944-d437ae686022)

**MySQL constraints**

NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, ENUM, SET

Example(foreign key constraint):
```
mysql> CREATE TABLE Authors(AuthorId INTEGER PRIMARY KEY, Name VARCHAR(70))
    -> type=InnoDB;
...
mysql> CREATE TABLE Books(BookId INTEGER PRIMARY KEY, Title VARCHAR(50),
    -> AuthorId INTEGER, FOREIGN KEY(AuthorId) REFERENCES Authors(AuthorId))
    -> type=InnoDB;
...
```
Example(set constraint):
```
mysql> CREATE TABLE Students(Id INTEGER, Name VARCHAR(55), 
    -> Certificates SET('A1', 'A2', 'B1', 'C1')); 
...
mysql> INSERT INTO Students VALUES(1, 'Paul', 'A1,B1');
mysql> INSERT INTO Students VALUES(2, 'Jane', 'A1,B1,A2');
mysql> INSERT INTO Students VALUES(3, 'Mark', 'A1,A2,D1,D2');
mysql> SELECT * FROM Students;
+------+------+--------------+
| Id   | Name | Certificates |
+------+------+--------------+
|    1 | Paul | A1,B1        |
|    2 | Jane | A1,A2,B1     |
|    3 | Mark | A1,A2        |
+------+------+--------------+
```
**Joins**
1. Inner join: returns all records that exist in both tables that match the ON condition.
![inner-join](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/465c9b3b-bc62-457c-91af-133e18e14c5f)

Syntax:
```
SELECT *
FROM table1
INNER JOIN table2
ON table1.col1 = table2.col2;
```

2. Full [outer] join: returns all the records that match the ON condition, no matter which table they are stored in.
![full-join](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/7b95d00f-4c22-4ab4-9276-6ac0eb3d8760)

Syntax:
```
SELECT *
FROM table1
FULL JOIN table2
ON table1.col1 = table2.col2;
```

3. FULL [OUTER] JOIN without the intersection: returns all records that match the ON condition, excluding those records exist in both tables.
![full-outer-join-no-intersection](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/ac82a33c-0f0d-425d-b59d-311f1673f058)

Syntax:
```
SELECT *
FROM table1
FULL JOIN table2
ON table1.col1 = table2.col2
WHERE table1.col1 IS NULL
OR table2.col2 IS NULL;
```

4. LEFT [OUTER] JOIN: returns all records from the left table (table1) that matched the ON condition.
![left-join](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/26577cc6-18b9-4d7c-9ded-5cb5de65fe54)

Syntax:
```
SELECT *
FROM table1
LEFT JOIN table2
ON table1.col1 = table2.col2;
```

5. LEFT [OUTER] JOIN without the intersection: returns all records from the left table (table1) that matched the ON condition, but exclude those are in common better two tables, or those records exist in both tables.
![left-join-no-intersection](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/4255afe4-cec1-475b-a3da-b526290ce698)

Syntax
```
SELECT *
FROM table1
LEFT JOIN table2
ON table1.col1 = table2.col2
WHERE table2.col2 IS NULL;
```

6. RIGHT [OUTER] JOIN: returns all records from the right table (table2) that matched the ON condition.
![right-join](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/7ccd9406-3c54-4868-acc3-79807325f285)

Syntax:
```
SELECT *
FROM table1
RIGHT JOIN table2
ON table1.col1 = table2.col2;
```

7. RIGHT [OUTER] JOIN without the intersection: returns all records from the right table (table2) that matched the ON condition, but exclude those are in common better two tables, or those records exist in both tables.
![right-join-no-intersection](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/d4bb24bc-9cb4-4e4e-b7e7-4bcdf978a808)

Syntax:
```
SELECT *
FROM table1
RIGHT JOIN table2
ON table1.col1 = table2.col2
WHERE table1.col1 IS NULL;
```

## Tasks
