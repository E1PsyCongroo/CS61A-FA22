# Return

def end(n, d):
    """Print the final digits of N in reverse order until D is found.

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None

def search(f):
    """Return the smallest non-negative integer x for which f(x) is a true value."""
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def square(x):
    return x * x

def triple(x):
    return 3 * x

def inverse(f):
    """Return a function g(y) that returns x such that f(x) == y.

    >>> sqrt = inverse(square)
    >>> sqrt(16)
    4
    >>> inverse(triple)(15)
    5
    """
    return lambda y: search(lambda x: f(x) == y)


def if_(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    """Return the real part of the square root of x.

    >>> real_sqrt(4)
    2.0
    >>> real_sqrt(-4)
    0.0
    """
    if x > 0:
        return sqrt(x)
    else:
        return 0.0
    # if_(x > 0, sqrt(x), 0.0)

# Control Expressions

def has_big_sqrt(x):
    """Return whether x has a big square root.

    >>> has_big_sqrt(1000)
    True
    >>> has_big_sqrt(100)
    False
    >>> has_big_sqrt(0)
    False
    >>> has_big_sqrt(-1000)
    False
    """
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    """Is N small enough that 1/N can be represented?

    >>> reasonable(100)
    True
    >>> reasonable(0)
    True
    >>> reasonable(-100)
    True
    >>> reasonable(10 ** 1000)
    False
    """
    return n == 0 or 1/n != 0.0

# Errors & Tracebacks

def f(x):
    return g(x - 1)

def g(y):
    return abs(h(y) - h(1 / y))  # remove paren

def h(z):
    return z * z  # remove return

print(f(12))  # remove 2
