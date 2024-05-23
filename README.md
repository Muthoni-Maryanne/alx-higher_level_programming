# Python

This section covers Python programming.

## Concepts
1. [The Python tutorial](https://docs.python.org/3.4/tutorial/index.html)
2. [Python Programming: An Introduction to Computer Science 3rd edition](https://nibmehub.com/opac-service/pdf/read/Python%20Programming%20_%20an%20introduction%20to%20computer%20science-%203rd%20Edition.pdf)
3. [Derek Banas’ Learn to program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
4. [The Python Guru](https://thepythonguru.com/)
5. [New string formatting](https://pyformat.info/)
6. [Garbage collector](https://thp.io/2012/python-gc/python_gc_final_2012-01-22.pdf)
7. [Python Interpreter](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
8. [Python bytecode](https://docs.python.org/3.4/library/dis.html)

## Projects

| No.  |Project       | Description    |
|------|--------------| ---------------|
|0.    | [0x00-python-hello_world](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/tree/main/0x00-python-hello_world) | This is the beginning of Python. Concepts covered include: the python interpreter, numbers, strings, indexing, slicing and string interpolation using %, .format and fstrings.|
|1.    |               |               |
|2.    |               |               |
|3.    |               |               |
|4.    |               |               |
|5.    |               |               |
|6.    |[0x06-python-classes](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/tree/main/0x06-python-classes)  | Concepts: classes, instances/objects, methods, class variables, instance variables, \_\_init__, self, encapsulation and its methods: getters and setters, pythonic way of dealing with private attributes which include @property and @<function_name>.setter, special operators e.g \_\_add__, \_\_sub__ etc.  |

# SQL
Requirements

- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

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
## Projects

| No.  |Project       | Description    |
|------|--------------| ---------------|
|0.    | [0x00-python-hello_world](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/tree/main/0x00-python-hello_world) | This is the beginning of Python. Concepts covered include: the python interpreter, numbers, strings, indexing, slicing and string interpolation using %, .format and fstrings.|
