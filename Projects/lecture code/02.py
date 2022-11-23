# Call expressions
max(2, 3)
min(1, -2, 3, -4, 5)
pow(100, 2)
pow(2, 100)

# Imports
from math import pi
pi * 71 / 223
from math import sin
sin(pi/2)

# Assignment
radius = 10
2 * radius
area, circ = pi * radius * radius, 2 * pi * radius
radius = 20

# Function values
max
max(3, 4)
f = max
f
f(3, 4)
max = 7
f(3, 4)
f(3, max)
f = 2
# f(3, 4)
__builtins__.max

# User-defined functions
from operator import add, mul

def square(x):
    return mul(x, x)

square(21)
square(add(2, 5))
square(square(3))

def sum_squares(x, y):
    return add(square(x), square(y))
sum_squares(3, 4)
sum_squares(5, 12)

# area function
def area():
    return pi * radius * radius
area()
radius = 20
area()
radius = 10
area()

# Name conflicts
def square(square):
    return mul(square, square)
square(4)
