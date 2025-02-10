For this tutorial, we are going to use `sqlite3` as our database provider.
# Creating a connection

import `sqlite3` from the package.
To create a connection, use the `connect` method from the library.
Assign `:memory:` as the connect argument, to allocate memory for the cursor pointer.

```python
import sqlite3 as sql

db = sql.connect(":memory:")
```
## Creating a cursor

The sqlite3cursor class is an instance using which you can invoke methods that execute SQLite statements, fetch data from the result sets of the queries.
This acts like a memory pointer for the database.

```python
cursor = db.cursor()
```

# Executing queries with sqlite3

The queries can be executed by using the `execute` method in cursor class.
The result of the latest query is stored in the latest cursor instance and can be fetched using `fetchall` method. 

```python
def run_query(query):
  cursor.execute(query)
  return cursor.fetchall()

result = run_query("SELECT * FROM employee")
print(result)
```

# Example

```python
import sqlite3 as sql

db = sql.connect(":memory:")
cursor = db.cursor()

def run_query(query):
  cursor.execute(query)
  return cursor.fetchall()

queries = [
    '''
    CREATE TABLE student (
      roll_no int PRIMARY KEY,
      name VARCHAR(50),
      subject VARCHAR(50),
      age INT
    )
    ''',
    "PRAGMA table_info(student)", # SQLite3 equivalent of MySQL's DESCRIBE TABLE
    "INSERT INTO student VALUES (1, 'Akshat', 'DBMS', 21)",
    "INSERT INTO student VALUES (2, 'Saksham', 'DBMS', 21)",
    "INSERT INTO student VALUES (3, 'Tichita', 'Cloud Computing', 21)",
    "INSERT INTO student VALUES (4, 'Varun', 'DL', 23)",
    "INSERT INTO student VALUES (5, 'Pranav', 'Cloud Computing', 22)",
    "SELECT * FROM student",
    '''
    SELECT name, age
    FROM student
    WHERE age <= 22
    ''',
    '''
    UPDATE student
    SET subject='ADBMS'
    WHERE subject='DBMS'
    ''',
    '''
    SELECT subject, COUNT(*)
    FROM student
    GROUP BY subject
    '''
]

for x in queries:
  result = run_query(x)
  print(result)

db.close()
```

