# calculator to make
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b
def power(a, b):
    return a ** b
def square_root(a):
    if a < 0:
        return "Error! Square root of negative number."
    return a ** 0.5
def factorial(n):
    if n < 0:
        return "Error! Factorial of negative number."
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def modulus(a, b):
    return a % b
def floor_divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a // b
def percentage(a, b):
    return (a / b) * 100
def logarithm(a, base):
    import math
    if a <= 0 or base <= 1:
        return "Error! Invalid input for logarithm."
    return math.log(a, base)
def sine(angle):
    import math
    return math.sin(math.radians(angle))
def cosine(angle):
    import math
    return math.cos(math.radians(angle))
def tangent(angle):
    import math
    return math.tan(math.radians(angle))

def main():
        