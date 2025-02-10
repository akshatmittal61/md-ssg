# I/O functions

```python
print("Akshat")
print(7)
print("Akshat", 7)

a = input("Enter your name: ")
b = int(input("Enter a number: "))
```
# Comparison function

```python
a = int(input("1st number: "))
b = int(input("2nd number: "))
c = int(input("3rd number: "))

ans1 = max(a, max(b, c))
ans2 = min(a, min(b, c))

print("Maximum number: ", ans1)
print("Minimum number: ", ans2)
```

# Range function

**Syntax**: 

```python
range_(start, stop, step_)
```

|Parameter|Description|
|---|---|
|_start_|Optional. An integer number specifying at which position to start. Default is 0|
|_stop_|Required. An integer number specifying at which position to stop (not included).|
|_step_|Optional. An integer number specifying the incrementation. Default is 1|

```python
print (list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print (list(range(0,20)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print (list(range(10,20)))
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print (list(range(0,20,2)))
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print (list(range(-10,-20,2)))
# []

print (list(range(-10,-20,-2)))
# [-10, -12, -14, -16, -18]
```

# Sum function
**Syntax :** sum(iterable, start)  

- **iterable** : iterable can be anything list , tuples or dictionaries , but most importantly it should be numbers.
- **start :** this start is added to the sum of  numbers in the iterable. If start is not given in the syntax , it is assumed to be 0.

```python
print(sum([1,2,3]))
# 6

print(sum(2,3))
# Error

print (sum(range(1,11)))
# 55

print(sum(range(1,11), 5))
# 60
```

# User defined functions

User can define their own functions using `def` keyword

```python
def isPrime(n):
  for i in range (2, n):
    if n % i == 0:
      return False
  return True
  
n = int(input("Enter a number: "))
print(f"{n} is {'a' if isPrime(n) else 'not a'} prime number")
```

# Lambda Functions

Lambda functions are inline / anonymous functions.