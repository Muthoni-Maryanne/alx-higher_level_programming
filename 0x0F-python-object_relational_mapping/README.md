# 0x0F. Python - Object-relational mapping

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
## Resources
1. [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
2. [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://mysqlclient.readthedocs.io/)
3. [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
4. [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
5. []()
## Summary
![extra 1](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/27d13c18-b77b-467d-9b68-561abcee1ce1)

![extra 2](https://github.com/Muthoni-Maryanne/alx-higher_level_programming/assets/107298263/47fe7c5d-994b-4e5b-bc11-694039eafb8b)
