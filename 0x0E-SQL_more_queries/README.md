# 0x0E. SQL - More queries
This is a continuation of SQL.
## Resources
1. [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
2. [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
3. [MySQL constraints](https://zetcode.com/mysql/constraints/)
4. [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
5. [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
6. 
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
