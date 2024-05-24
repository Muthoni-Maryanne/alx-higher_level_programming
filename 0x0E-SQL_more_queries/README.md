# 0x0E. SQL - More queries
This is a continuation of SQL.
## Resources
1. [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
2. [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-administration/mysql-grant/)
3. []()
## Summary
**Create a New User and Grant Permissions in MySQL**
1. Log into MySQL server: ```$ sudo mysql``` if using auth_socket or ```$ sudo -u root -p``` if using password
2. Create user: ```$ CREATE USER 'username'@'host' IDENTIFIED WITH authentication_plugin BY 'password';``` to create a user that authenticates with auth_socket or ```$ CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';``` to create a user that authenticates with caching_sha2_password.
3. Grant permission. Syntax: ```GRANT PRIVILEGE ON database.table TO 'username'@'host';```

Example- Grants a user global privileges to CREATE, ALTER, and DROP databases, tables, and users, as well as the power to INSERT, UPDATE, and DELETE data from any table on the server. It also grants the user the ability to query data with SELECT, create foreign keys with the REFERENCES keyword, and perform FLUSH operations with the RELOAD privilege: 

```GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;```

Example to grant all permissions globally: ```GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;```

4. Flush privileges to to reload the grant tables to ensure that the new privileges are put into effect:```FLUSH PRIVILEGES;```
5. Exit: ```exit```
6. Log in in future: ```mysql -u sammy -p```

- To revoke permissions: ```REVOKE type_of_permission ON database_name.table_name FROM 'username'@'host';```
- Review a user’s current permissions: ```SHOW GRANTS FOR 'username'@'host';```
- Delete a user: ```DROP USER 'username'@'localhost';```

