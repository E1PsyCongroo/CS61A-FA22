def iterator_demos():
    """Using iterators

    >>> s = [[1, 2], 3, 4, 5]
    >>> next(s)
    Traceback (most recent call last):
        ...
    TypeError: 'list' object is not an iterator
    >>> t = iter(s)
    >>> next(t)
    [1, 2]
    >>> next(t)
    3
    >>> u = iter(s)
    >>> next(u)
    [1, 2]
    >>> list(t)
    [4, 5]
    >>> next(t)
    Traceback (most recent call last):
        ...
    StopIteration
    >>> d = {'one': 1, 'two': 2, 'three': 3} # Keys and values
    >>> k = iter(d) # next(k)
    >>> v = iter(d.values()) # next(v)
    >>> k = iter(d)
    >>> d.pop('two')
    2
    >>> next(k)
    Traceback (most recent call last):
        ...
    RuntimeError: dictionary changed size during iteration
    >>> r = range(3, 6)
    >>> s = iter(r)
    >>> next(s)
    3
    >>> for x in s:
    ...     print(x)
    4
    5
    >>> for x in s:
    ...     print(x)
    >>> for x in r:
    ...    print(x)
    3
    4
    5
    >>> for x in r:
    ...    print(x)
    3
    4
    5
    """

def double(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

def built_in_demo():
    """Using built-in sequence functions.

    >>> bcd = ['b', 'c', 'd']
    >>> [x.upper() for x in bcd]
    ['B', 'C', 'D']
    >>> caps = map(lambda x: x.upper(), bcd)
    >>> next(caps)
    'B'
    >>> next(caps)
    'C'
    >>> s = range(3, 7)
    >>> doubled = map(double, s)
    >>> next(doubled)
    *** 3 => 6 ***
    6
    >>> next(doubled)
    *** 4 => 8 ***
    8
    >>> list(doubled)
    *** 5 => 10 ***
    *** 6 => 12 ***
    [10, 12]
    >>> f = lambda x: x < 10
    >>> a = filter(f, map(double, reversed(s)))
    >>> list(a)
    *** 6 => 12 ***
    *** 5 => 10 ***
    *** 4 => 8 ***
    *** 3 => 6 ***
    [8, 6]
    >>> t = [1, 2, 3, 2, 1]
    >>> reversed(t) == t
    False
    >>> list(reversed(t)) == t
    True
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> items = zip(d.keys(), d.values()) # Call next(items)
    """

# Zip

def palindrome(s):
    """Return whether s is the same sequence backward and forward.

    >>> palindrome([3, 1, 4, 1, 5])
    False
    >>> palindrome([3, 1, 4, 1, 3])
    True
    >>> palindrome('seveneves')
    True
    >>> palindrome('seven eves')
    False
    """
    # return s == reversed(s)  # This version doesn't work
    return all([a == b for a, b in zip(s, reversed(s))])
    return list(s) == list(reversed(s))

# Blackjack

import random

points = {'J': 10, 'Q': 10, 'K':10, 'A': 1}

def hand_score(hand):
    """Total score for a hand.

    >>> hand_score(['A', 3, 6])
    20
    >>> hand_score(['A', 'J', 'A'])
    12
    """
    total = sum([points.get(card, card) for card in hand])
    if total <= 11 and 'A' in hand:
        return total + 10
    return total

def shuffle_cards():
    deck = (['J', 'Q', 'K', 'A'] + list(range(2, 11))) * 4
    random.shuffle(deck)
    return iter(deck)

def basic_strategy(up_card, cards):
    if hand_score(cards) <= 11:
        return True
    if up_card in [2, 3, 4, 5, 6]:
        return False
    return hand_score(cards) < 17

def player_turn(up_card, cards, strategy, deck):
    while hand_score(cards) <= 21 and strategy(up_card, cards):
        cards.append(next(deck))

def dealer_turn(cards, deck):
    while hand_score(cards) < 17:
        cards.append(next(deck))

def blackjack(strategy, announce=print):
    """Play a hand of casino blackjack."""
    deck = shuffle_cards()

    player_cards = [next(deck)]
    up_card = next(deck)
    player_cards.append(next(deck))
    hole_card = next(deck)

    player_turn(up_card, player_cards, strategy, deck)
    if hand_score(player_cards) > 21:
        announce('Player goes bust with', player_cards,
                 'against a', up_card)
        return -1

    dealer_cards = [up_card, hole_card]
    dealer_turn(dealer_cards, deck)
    if hand_score(dealer_cards) > 21:
        announce('Dealer busts with', dealer_cards)
        return 1
    else:
        announce('Player has', hand_score(player_cards),
                 'and dealer has', hand_score(dealer_cards))
        diff = hand_score(player_cards) - hand_score(dealer_cards)
        return max(-1, min(1, diff))

def shhh(*args):
    "Don't print (or do anything else)."

def gamble(strategy, hands=1000):
    return sum([blackjack(strategy, shhh) for _ in range(hands)])

