Strings are a collection of characters.

# Declaration

Strings can be declared using *double* or *single* quotes identically.

```python
s = "Hello World"
print(s)
# Hello World

s = 'Helllo World'
print(s)
# Hello World
```

# Indexing

## Access character by index

```python
var1 = "123456789"

print(var1)
# 123456789

print(var1[1])
# 2

print(var1[2])
# 3

print(var1[-1])
# 9

print(var1[-2])
# 8
```

## Access character range by `:`

- For $[x:y]$  range from $x$ t o $y-1$ is returned
- For $[x:]$ range from $x$ to the end is returned
- For $[:x]$ range from beginning to  $x$ is returned
- Result is always retuned from LTR format of elements arrangement in the string

```python
var1 = "123456789"

print(var1)
# 123456789

print(var1[1:3])
# 23

print(var1[2:])
# 3456789

print(var1[2:5])
# 345

print(var1[:2])
# 12

print(var1[:-1])
# 12345678

print(var1[-4:-1])
# 678
```

# String functions

```python
s = "Hello World"

print("Length of s: ", len(s))
# Length of s: 11

print("s in upper case: ", s.upper())
# s in upper case: HELLO WORLD 

print("s in lower case: ", s.lower())
# s in lower case: hello world

print("  Hello World  ".strip())
# Hello World

```

# String formatting

## Formatters $(\%)$
```python
name  = input("Enter your name: ")
age   = int(input("Enter your age: "))
price = float(input("Enter the book price: "))

s = "Your name is %s, age is %d and book price is %f" %(name.upper(),age,price)

print (s)
# You name is Akshat, age is 21 and book price is 600.000000

```

```python
first_name = 'akshat'  
last_name = 'mittal'  
print('Hello! My name is ' + first_name.capitalize() + ' ' + last_name.capitalize())  
print('Hello! My name is {} {}'.format(first_name, last_name))  
print('Hello! My name is {1} {0}'.format(last_name, first_name))  
print(f'Hello! My name is {first_name} {last_name}')

# They all will print same string
# Hello! My name is Akshat Mittal
# .capitalize() changes first letter to capital and rest to small
```
## Multiple line strings $(""")$

```python
para_str = """This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""

print (para_str)

# This is a long string that is made up of several lines and non-printable characters such as TAB ( ) and they will show up that way when displayed. NEWLINEs within the string, whether explicitly given like this within the brackets [ ], or just a NEWLINE within the variable assignment will also show up.
```

