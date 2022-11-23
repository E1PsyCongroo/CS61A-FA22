# Functional arguments

def apply_twice(f, x):
    """Return f(f(x))

    >>> apply_twice(square, 2)
    16
    >>> from math import sqrt
    >>> apply_twice(sqrt, 16)
    2.0
    """
    return f(f(x))

def square(x):
    return x * x

result = apply_twice(square, 2)

# Functional return values

def make_adder(n):
    """Return a function that takes one argument k and returns k + n.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder

# Lexical scope and returning functions

def f(x, y):
    return g(x)

def g(a):
    return a + y

# This expression causes an error because y is not bound in g.
# f(1, 2)

# Composition

def compose1(f, g):
    """Return a function that composes f and g.

    f, g -- functions of a single argument
    """
    def h(x):
        return f(g(x))
    return h

def triple(x):
    return 3 * x

squiple = compose1(square, triple)
tripare = compose1(triple, square)
squadder = compose1(square, make_adder(2))

# Lambda expressions

x = 10
square = x * x
square = lambda x: x * x
square(4)

# Currying

from operator import add, mul

def curry2(f):
    """Curry a two-argument function.

    >>> m = curry2(add)
    >>> add_three = m(3)
    >>> add_three(4)
    7
    >>> m(2)(1)
    3
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
