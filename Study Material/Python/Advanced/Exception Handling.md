Exceptional handling in Python is done by three keywords, `try` -> `except` -> `finally`

```python
try:  
    n1 = int(input('Enter num 1: '))  
    n2 = int(input('Enter num 2: '))  
    print(f'Add: {n1 + n2}')  
except ValueError as e:  
    print(e)  
finally:  
    print('Done with it')
```

Here, `ValueError` can be replaced by the type of error that might occur in the code snippet.