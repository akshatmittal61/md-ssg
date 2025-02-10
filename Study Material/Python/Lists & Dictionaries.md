# Lists

Array in python is knows as a list

```python
fruits = ['Apple', 'Mango', 'Banana']
print(fruits)
```

## Adding to lists

```python
fruits = ['Apple', 'Mango', 'Banana']
fruits.append('Papaya')  
fruits.insert(1, 'Pineapple')
print(fruits)
# Apple Pineapple Mango Banana Papaya
```

## Sorting a list

The sort function in python works in place for lists.

```python
fruits.sort()
# Apple Banana Mango Papaya Pineapple
```

## List clipping

```python
print(fruits)
# Apple Banana Mango Papaya Pineapple
print(fruits[1])
# Banana
print(fruits[:3])
# ['Apple', 'Banana', 'Mango']
print(fruits[1:3])
# ['Banana', 'Mango']
print(fruits[-1])
# Pineapple
print(fruits[-1:-3])
# []
print(fruits[-3:-1])
# ['Mango', 'Papaya']
```


# Dictionaries


JSON object can be created in python using key-value pair collections.

```python
user = {  
    'name': 'Akshat',  
    'age': 21,  
    'stack': 'full',  
    'tags': ['developer', 'poet', 'hunter']  
}  

user['weather'] = 'fall'
print(user, len(user))

# {'name': 'Akshat', 'age': 21, 'stack': 'full', 'tags': ['developer', 'poet', 'hunter'], 'weather': 'fall'} 5 3

```
