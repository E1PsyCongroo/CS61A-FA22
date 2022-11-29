def factorial_rec(n, k):
    """Return k * n!

    >>> factorial_rec(5, 3)
    360
    """
    if n == 0:
        return k
    return factorial_rec(n-1, k*n)

def factorial_iter(n, k):
    """Return k * n!

    >>> factorial_iter(5, 3)
    360
    """
    while n > 0:
        n, k = n-1, k*n
    return k

