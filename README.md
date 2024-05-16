# CRUD Operations using Tortoise ORM and MySQL

`tortoiseorm-crud` is a Python script that performs CRUD operations using Tortoise ORM (Object Relational Mapper) and MySQL. 

ORM stands for Object-Relational Mapping. It is a programming technique for converting data between incompatible systems using object-oriented programming languages. In the context of databases, ORM allows the representation of relational data in object-oriented programming languages. This means that instead of writing SQL queries to interact with a database, developers can use objects and methods to perform the same operations, making it easier to work with databases in an object-oriented way.

Tortoise ORM is an easy-to-use asyncio ORM (Object-Relational Mapping) inspired by Django ORM. It provides a straightforward way to work with databases in Python, allowing developers to define database models and interact with the database using Python code. Tortoise ORM supports various database backends such as PostgreSQL, MySQL, and SQLite, and it is designed to work seamlessly with asyncio, making it suitable for building asynchronous applications.

## Usage
### MySQL database setting
Edit `db_url` and replace the username and password. Replace `kamusi` with the name you want to give to your database. 
To create a database in MySQL, you can use the following SQL command:
```sql
CREATE DATABASE database_name;
```
This command creates a new database with the specified name in your MySQL server. For other MySQL commends, go to [MySQL Cheatsheet](https://github.com/easai/mysql-cheatsheet).

### Install Tortoise ORM
To install Tortoise ORM, you can use the following command:
```bash
pip install tortoise-orm
```

### Execute the code
To execute the code, you can use the following command:
```bash
py kamusi.py
```
The code uses Tortoise ORM to perform CRUD (Create, Read, Update, Delete) operations on a "Kamusi" model. Here's a brief explanation of each operation:

1. **Create**: The `Kamusi.create()` method creates a new dictionary record in the database.

2. **Read**: The `Kamusi.all()` method retrieves all records from the database and prints them.

3. **Update**: The `Kamusi.filter().update` method updates the `en` field of the record with a specified ID.

4. **Delete**: The `Kamusi.filter().delete` method deletes a record with a specified ID from the database.

The code also initializes the Tortoise ORM, connects to the MySQL database, generates the necessary schemas, and closes the database connection after the operations are complete.
