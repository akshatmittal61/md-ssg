
# Arithmetic Operators

1. $+$ : Add two numbers
2. $-$ : Subtract two numbers
3. $*$ : Multiply two numbers
4. $/$ : Divide two numbers
5. $//$ : Floor division
6. $**$ : Exponentiation

# Bitwise operators

1. $|$: Bitwise OR
2. $\&$: Bitwise AND
3. $\sim$: Bitwise NOT
4. $>>$: Bitwise right shift, pops out the last bit
5. $<<$: Bitwise left shift, pops out the first bit

# Type casting and Concatenation

```python
print(int("Akshat"))
# Error

print(int("20107"))
# 20107

print(str("Akshat"))
# Akshat

print(str(20107))
# 20107

print(str("akshat")+20107)
# Error

print(str(20107)+"akshat")
# 20107Akshat

print(int(20107)+"akshat")
# Error

print(int(45.20))
# 45

print(str(int(45.20))+"akshat")
# 45akshat
```

# Logical Operators

1. $and$: Logical AND between two conditions
2. $or$: Logical OR between two conditions
3. $not$: logical NOT for a condition -> always returns Boolean result
```python
not True
# False
not 1
# False
```

## Identity Operators

1. $is$: is equal to, analog for `==`
2. $is \ not$: is not equal to, analog for `!=`

## Membership Operators

Used with iterable data types -> list, object
1. $in$: is contained inside
2. $not in$: is not contained inside