# Libraries
A Python library is a collection of related modules. It contains bundles of code that can be used repeatedly in different programs

```python
import math
print("Square root of 25: ", math.sqrt(25))
```

```python
import math as m
print("Square root of 25: ", m.sqrt(25))
```

```python
from math import sqrt
print("Square root of 25: ", sqrt(25))
```
# Math Library

## Math Methods

|Method|Description|
|---|---|
|math.ceil()|Rounds a number up to the nearest integer|
|math.cos()|Returns the cosine of a number|
|math.degrees()|Converts an angle from radians to degrees|
|math.fabs()|Returns the absolute value of a number|
|math.factorial()|Returns the factorial of a number|
|math.floor()|Rounds a number down to the nearest integer|
|math.fmod()|Returns the remainder of x/y|
|math.gcd()|Returns the greatest common divisor of two integers|
|math.isnan()|Checks whether a value is NaN (not a number) or not|
|math.isqrt()|Rounds a square root number downwards to the nearest integer|
|math.log()|Returns the natural logarithm of a number, or the logarithm of number to base|
|math.log10()|Returns the base-10 logarithm of x|
|math.log2()|Returns the base-2 logarithm of x|
|math.pow()|Returns the value of x to the power of y|
|math.radians()|Converts a degree value into radians|
|math.sin()|Returns the sine of a number|
|math.sqrt()|Returns the square root of a number|
|math.tan()|Returns the tangent of a number|

## Math Constants

|Constant|Description|
|---|---|
|math.e|Returns Euler's number (2.7182...)|
|math.pi|Returns PI (3.1415...)|



# Requirements File

Many projects rely on libraries and other dependencies, and installing each one can be tedious and time-consuming.
This is where a `requirements.txt` file comes into play. `requirements.txt` is a file that contains a list of packages or libraries needed to work on a project that can all be installed with the file.

## Generating file

To generate a `requirements.txt` from currently installed dependencies:

```sh
pip freeze > requirements.txt
```

## Installing dependencies

To install dependencies in a project having existing `requirements.txt` file:
```bash
pip install -r requirements.txt
```

