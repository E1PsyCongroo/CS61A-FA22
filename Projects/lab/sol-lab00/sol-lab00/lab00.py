def twenty_twenty_two():
    """Come up with the most creative expression that evaluates to 2022,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_two()
    2022
    """
    return ((20 ** 2 + 22 ** 2) + ((2 ** 0 + 2 ** 2) * 20 * 22) + (20 + 2 * 2) * 20 * 2) // 2
