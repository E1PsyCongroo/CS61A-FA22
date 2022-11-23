# Slicing

odds = [3, 5, 7, 9, 11]
list(range(1, 3))
[odds[i] for i in range(1, 3)]
odds[1:3]
odds[1:]
odds[:3]
odds[:]

# Aggregation

sum(odds)
sum({3: 9, 5: 25})
max(range(10))
max(range(10), key=lambda x: 7 - (x - 2) * (x - 4))
all([x < 5 for x in range(5)])
perfect_square = lambda x: x == round(x ** 0.5) ** 2
any([perfect_square(x) for x in range(50, 60)])  # Try ,65)


# Dicts

def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    # numerals['X-ray']
    # numerals[10]
    len(numerals)
    list(numerals)
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([[3, 9], [4, 16]])
    numerals.get('X', 0)
    numerals.get('X-ray', 0)
    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}


def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which
    match(k, v) is a true value.

    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}
