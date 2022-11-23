# Self-Reference

def print_all(k):
    """Print all arguments of repeated calls.

    >>> f = print_all(1)(2)(3)(4)(5)
    1
    2
    3
    4
    5
    """
    print(k)
    return print_all

def print_sums(n):
    """Print all sums of arguments of repeated calls.

    >>> f = print_sums(1)(2)(3)(4)(5)
    1
    3
    6
    10
    15
    """
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

# Sum digits

def split(n):
    """Split a positive integer into all but its last digit and its last digit."""
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n.

    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    >>> sum_digits(11408855402054064613470328848384)
    126
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

# Iteration vs recursion

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# Luhn algorithm: mutual recursion

def luhn_sum(n):
    """Return the digit sum of n computed by the Luhn algorithm.

    >>> luhn_sum(2)
    2
    >>> luhn_sum(12)
    4
    >>> luhn_sum(42)
    10
    >>> luhn_sum(138743)
    30
    >>> luhn_sum(5105105105105100) # example Mastercard
    20
    >>> luhn_sum(4012888888881881) # example Visa
    90
    >>> luhn_sum(79927398713) # from Wikipedia
    70
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    """Return the Luhn sum of n, doubling the last digit."""
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

# Converting iteration to recursion

def sum_digits_iter(n):
    """Sum digits iteratively.

    >>> sum_digits_iter(11408855402054064613470328848384)
    126
    """
    digit_sum = 0
    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last
    return digit_sum

def sum_digits_rec(n, digit_sum):
    """Sum digits using recursion, based on iterative version.

    >>> sum_digits_rec(11408855402054064613470328848384, 0)
    126
    """
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)


