# 0x0D. SQL - Introduction

This is an introduction to relational data bases.

# Resources
1. [How to Install MySQL on Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)
2. [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)
3. []()
4. []()
5. []()
6. []()
7. []()
8. []()
9. []()
10. []()

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

# Tasks
