# If-Else-If

```python
if a > b:
	print("a is greater than b")
elif a == b:
	print("a is equal to b")
else:
	print("a is smaller than b")
```

# Loops

## While Loop

```python
i = 1
while i <= 10:
    print (i)
    i += 1
```

## For loop

```python
for x in [7, 13, 19, 23]:
	print(2*x)
```


```python
for i in range(1,21,2):
    print (i)
```

```python
people = ['Jane', 'Kate', 'Christopher', 'Fiona']

for person in people:
    print(person.capitalize())

'''
Jane
Kate
Christopher
Fiona
'''
```

For `range` function, refer [[Functions#Range function]]

- To print table by range

```python
a = int(input("Enter a number: "))
for i in range(1, 10):
	print(a, ' * ', i, ' = ', a * i)
```

- To generate username by name and employee id

```python
def generate_username(name, emp_id):
    first_char = name.split()[0][0].lower()
    second_char = name.split()[1][0].lower()
    num_id = emp_id[-3:]
    return first_char + second_char + num_id


username = generate_username('Jane doe', 'emp102947')
print(username)
# jd947
```