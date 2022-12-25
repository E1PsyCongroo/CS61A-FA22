class Tree:
    def __init__(self, label, branches=[]):
        for branch in branches:
            assert isinstance(branch, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches


def bigs(t):
    """Return the number of nodes in t that are larger than all their ancestors.

    >>> p = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> bigs(p)
    5
    >>> q = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs(q)
    4
    """
    def f(a, x):
        if a.label > x:
            return 1 + sum([f(b, a.label) for b in a.branches])
        else:
            return sum([f(b, x) for b in a.branches])
    return f(t, t.label - 1)


def bigs_mutation(t):
    """Return the number of nodes in t that are larger than all their ancestors.

    >>> p = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> bigs_mutation(p)
    5
    >>> q = Tree(1, [Tree(4, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(2)])])])
    >>> bigs_mutation(q)
    4
    """
    n = [0]
    def f(a, x):
        if a.label > x:
            n[0] += 1
        for b in a.branches:
            f(b, max(a.label, x))
    f(t, t.label - 1)
    return n[0]


def smalls(t):
    """Return the non-leaf nodes in t that are smaller than all their descendants.

    >>> a = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(0, [Tree(6)])])])
    >>> sorted([t.label for t in smalls(a)])
    [0, 2]
    """
    result = []
    def process(t):
        # (a Tree t) -> (the smallest value within t)
        # side-effect: perhaps add t to result
        if t.is_leaf():
            return t.label
        else:
            smallest = min([process(b) for b in t.branches])
            if t.label < smallest:
                result.append(t)
            return min(smallest, t.label)
    process(t)
    return result
