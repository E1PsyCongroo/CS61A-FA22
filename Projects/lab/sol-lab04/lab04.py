HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n - 1, term)
    # Base case: only one item to sum, so we return that item.
    # Recursive call: returns the result of summing the numbers from 1 to n-1 using
    # term. All that's missing is term applied to the current value n.

    # Extra challenge: how might you implement this using a helper function?


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    if column == 0:
        return 1
    elif row == 0:
        return 0
    else:
        above = pascal(row - 1, column)
        above_left = pascal(row - 1, column - 1)
        return above + above_left
    # First base case: every number in the leftmost column of the triangle is 1.
    # Second base case: There is only one number in the topmost row, which is already
    # accounted for by the first base case.


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if m == 1 or n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)
    # Base case: Look at the two visual examples given. Since the insect
    # can only move to the right or up, once it hits either the very right side
    # or the top edge, it has already reached a unique path -- the insect has
    # no choice but to go straight up or straight right (respectively) at that point.
    # There is no way for it to backtrack by going left or down.

    # Alternative solution:
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    return paths(m - 1, n) + paths(m, n - 1)
    # This solution is similar to the alternate solution for Count Stair Ways from Discussion 4 --
    # if we reach the exact destination, we have found a unique path (first base case), but if
    # we overshoot, we have not found a valid path (second base case).

    # Notice, however, that this solution is not as short and simple as the first solution
    # since it doesn't make use of the insect's restricted movements (only right or up)
    # to cut the program short. We have to reach the exact destination for the second solution,
    # while in the first we just have to reach the right or top boundary.


def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    return [[s[i], t[i]] for i in range(0, len(s))]


def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    last, second_last = n % 10, n // 10 % 10
    if last == 8 and second_last == 8:
        return True
    elif n < 100:
        return False
    return double_eights(n // 10)

    # Alternate solution
    last, second_last = n % 10, n // 10 % 10
    if n < 10:
        return False
    return (last == 8 and second_last == 8) or double_eights(n // 10)


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[x, fn(x)] for x in seq if lower <= fn(x) <= upper]


def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    return [deck[(i % 2) * len(deck) // 2 + i // 2] for i in range(len(deck))]

# ALTERNATE SOLUTION


def riffle(deck):
    return [deck[i // 2] if i % 2 == 0 else deck[len(deck) // 2 + i // 2] for i in range(len(deck))]
