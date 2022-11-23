def errors():
    abs('hello') # TypeError
    hello # NameError
    {}['hello'] # KeyError
    def f(): f()
    f() # RecursionError

def double(x):
    if isinstance(x, str):
        raise TypeError('double takes only numbers')
    return 2 * x

def invert(x):
    """Return 1/x

    >>> invert(2)
    Never printed if x is 0
    0.5
    """
    result = 1/x  # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result

def invert_safe(x):
    """Return 1/x, or the string 'divison by zero' if x is 0.

    >>> invert_safe(2)
    Never printed if x is 0
    0.5
    >>> invert_safe(0)
    'division by zero'
    """
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)

from operator import add, mul, truediv
def reduce(f, s, initial):
    """Combine elements of s pairwise using f, starting with initial.

    >>> reduce(mul, [2, 4, 8], 1)
    64
    >>> reduce(pow, [1, 2, 3, 4], 2)
    16777216
    """
    for x in s:
        initial = f(initial, x)
    return initial

def divide_all(n, ds):
    """Divide n by every d in ds.

    >>> divide_all(1024, [2, 4, 8])
    16.0
    >>> divide_all(1024, [2, 4, 0, 8])
    inf
    """
    try:
        return reduce(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')

