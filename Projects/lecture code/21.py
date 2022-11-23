def str_repr_demos():
    from fractions import Fraction
    half = Fraction(1, 2)
    half
    print(half)
    str(half)
    repr(half)

    s = 'hello world'
    str(s)
    repr(s)
    "'hello world'"
    repr(repr(repr(s)))
    eval(eval(eval(repr(repr(repr(s))))))
    # Errors: eval('hello world')


# Implementing generic string functions

class Bear:
    """A Bear.


    >>> oski = Bear()
    >>> oski
    Bear()
    >>> print(oski)
    a bear
    >>> print(str(oski))
    a bear
    >>> print(repr(oski))
    Bear()
    >>> print(oski.__repr__())
    oski
    >>> print(oski.__str__())
    oski the bear

    >>> print(str_(oski))
    a bear
    >>> print(repr_(oski))
    Bear()
    """

    def __init__(self):
        self.__repr__ = lambda: 'oski'  # instance attribute
        self.__str__ = lambda: 'oski the bear'

    def __repr__(self):  # class attribute
        return 'Bear()'

    def __str__(self):
        return 'a bear'


def print_bear():
    oski = Bear()
    print(oski)
    print(str(oski))
    print(repr(oski))
    print(oski.__repr__())
    print(oski.__str__())


def repr_(x):
    s = type(x).__repr__(x)
    if not isinstance(s, str):
        raise TypeError
    return s


def str_(x):
    s = type(x).__str__(x)
    if not isinstance(s, str):
        raise TypeError
    return s


def fstring_demos():
    """f-string demos.

    >>> f'2 + 2 = 2 + 2'
    '2 + 2 = 2 + 2'
    >>> f'2 + 2 = {2 + 2}'
    '2 + 2 = 4'
    >>> '2 + 2 = {2 + 2}'
    '2 + 2 = {2 + 2}'
    >>> f'2 + 2 = {abs(2 + 2)}'
    '2 + 2 = 4'
    >>> abs = float
    >>> f'2 + 2 = {abs(2 + 2)}'
    '2 + 2 = 4.0'
    >>> f'2 + 2 = {(lambda x: x + x)(2)}'
    '2 + 2 = 4'

    >>> from fractions import Fraction
    >>> half = Fraction(1, 2)
    >>> half
    Fraction(1, 2)
    >>> print(half)
    1/2
    >>> f'half of a half is {half * half}.'
    'half of a half is 1/4.'

    >>> s = [9, 8, 7]
    >>> f'because {s.pop()} {s.pop()} {s}'
    'because 7 8 [9]'
    """


# Ratio numbers
from fractions import gcd


class Ratio:
    """A mutable ratio.

    >>> f = Ratio(9, 15)
    >>> f
    Ratio(9, 15)
    >>> print(f)
    9/15

    >>> Ratio(1, 3) + Ratio(1, 6)
    Ratio(1, 2)
    >>> f + 1
    Ratio(8, 5)
    >>> 1 + f
    Ratio(8, 5)
    >>> 1.4 + f
    2.0
    """

    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        else:
            return float(self) + other
        g = gcd(n, d)
        r = Ratio(n // g, d // g)
        return r

    __radd__ = __add__

    def __float__(self):
        return self.numer / self.denom
