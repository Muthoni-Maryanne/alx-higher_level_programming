# 0x0D. SQL - Introduction

This is an introduction to relational data bases.

# Concepts
1. [Databases](https://intranet.alxswe.com/concepts/37)
2. [The big NoSQL databases comparison](http://kkovacs.eu/cassandra-vs-mongodb-vs-couchdb-vs-redis)
# Resources
1. [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
2. [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
3. [Basic SQL statements: DDL and DML](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)
4. [Basic queries: SQL and RA](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)
5. 
6. [How to Install MySQL on Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)
   


# Summary
**Installation on Ubuntu 20.04**

1. Update Ubuntu packages 
2. Install MySQL
3. Securing MySQL
- Run security script
- Enter password
- Choose password validation or not and if chosen pick level
- Press Y when satisfied with password
- Answer 'Y' to all security prompts(recommended)
4. Check if MySQL Service Is Running
5. Log in to MySQL Server.
- Use ```sudo mysql -u root``` if password authenticated or ```sudo mysql``` if set to authenticate using the auth_socket plugin.
6. Creating a Dedicated MySQL User and granting Privileges if not working in root user account.
7. Flush privileges to free up memory and exit.
8. To log in in future ```mysql -u sammy -p```
```
$ sudo apt update
...
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$ sudo mysql_secure_installation
...
$ sudo systemctl status mysql
...
$ sudo mysql -u root
...
mysql> CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';
...
mysql> GRANT PRIVILEGE ON database.table TO 'username'@'host';
...
mysql> FLUSH PRIVILEGES;
...
mysql> exit
...
```
Note: As of July 2022, an error will occur when you run the mysql_secure_installation script without some further configuration leading to a recursive loop.

This script will attempt to set a password for the installation’s root MySQL account but, by default on Ubuntu installations, this account is not configured to connect using a password. To fix need to first adjust how your root MySQL user authenticates. 

Below ALTER USER command to change the root user’s authentication method to one that uses a password. The following example changes the authentication method to mysql_native_password:
```
$ sudo mysql
...
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
...
mysql> exit
```
After this can run ```mysql_secure_installation``` without issue. After can then reopen MySQL and change the root user’s authentication method back to the default, auth_socket. To authenticate as the root MySQL user using a password, run this command: ```mysql> mysql -u root -p```. Then go back to using the default authentication method using this command:

```mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;```

**DDL and DML**

SQL statements are divided into two major categories: data definition language (DDL) and data manipulation language (DML). 


DDL statements are used to build and modify the structure of your tables and other objects in the database. When you execute a DDL statement, it takes effect immediately. Example of create table:
```
CREATE TABLE <table name> ( 
        <attribute name 1> <data type 1>,
        ...
        <attribute name n> <data type n>);
```
DML statements are used to work with the data in tables e.g., SELECT, UPDATE, INSERT, DELETE
```
INSERT INTO <table name>
        VALUES (<value 1>, ... <value n>);
```
```
UPDATE <table name>
        SET <attribute> = <expression>
        WHERE <condition>;
```
```
DELETE FROM <table name>
        WHERE <condition>;
```
**Basic queries: SQL and RA**

Retrieval of data in SQL- Syntax of SELECT statement:
```
SELECT {attribute}+
  FROM {table}+
  [ WHERE {boolean predicate to pick rows} ]
  [ ORDER BY {attribute}+ ];
```
# Tasks
