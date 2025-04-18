#https://github.com/bernardoalveslopes/lab10-BL-DC
# Partner 1: Bernardo Lopes
# Partner 2: Darryl Culver
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

# Partner info
# https://github.com/bernardoalveslopes/lab10-BL-DC
# Partner 1: Bernardo Lopes
# Partner 2: Darryl Culver

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b
