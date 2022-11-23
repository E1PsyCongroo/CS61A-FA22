'''
Curry Up Now
The function order_meal takes three arguments, item_price, item_quantity, and ordered_at, and either
returns the total cost of the meal or reports how many hours should be waited before ordering. Only the
doctests are shown below, as the implementation is not necessary for completing the question.

def order_meal(item_price, item_quantity, ordered_at):
    """
    >>> order_meal(5.99, 5, 11)
    29.95
    >>> order_meal(9.99, 5, 20)
    49.95
    >>> order_meal(8.99, 5, 7)
    'Wait!'
    """
    # Code intentionally omitted
Implement curry_up_now, a function that curries order_meal into a chain of three functions that each take a
single argument. Once the third function is called, it should attempt to order the meal and print out the result.
If the meal was successfully ordered during business hours, it should then return another curried function that
can re-order the same item with a 50% discount.

def curry_up_now(item_price):
    """
    >>> curry_up_now(2.99)(2)(15)
    5.98
    <function <lambda>>
    >>> lunch_special = curry_up_now(8.99)
    >>> lunch_special(5)(11)
    44.95
    <function <lambda>>
    >>> lunch_special(3)(13)(2)(14)
    26.97
    8.99
    >>> no_discount = curry_up_now(10.99)(4)(7)
    Wait!
    >>> print(no_discount)
    None
    """
def order_quantity(item_quantity):
    def by(ordered_at):
        result = ________
                    (a)
        ________
            (b)
        ________:
            (c)
            return ________
                    (d)
        return by
    return order_quantit

Rewrite the body of the inner by function in a single line of code, such that it behaves the same
and passes the same doctests. Note that two calls to order_meal with the same parameters will always
have the same result.
def curry_up_now(item_price):
    def order_quantity(item_quantity):
        def by(ordered_at):
            _____________________
            #answer:return print(order_now(item_price, item_quantity, ordered_at)) or ( (lambda q: lambda h: order_meal(item_price * 0.5, q, h)) if order_now(item_price, item_quantity, ordered_at) != "Wait!" else None)
        return by
    return order_quantity
A large text area is provided to give you ample space to write, but your answer must be a valid single line
of code.
'''


def order_meal(item_price, item_quantity, ordered_at):
    """
    >>> order_meal(5.99, 5, 11)
    29.95
    >>> order_meal(9.99, 5, 20)
    49.95
    >>> order_meal(8.99, 5, 7)
    'Wait!'
    """
    # Code intentionally omitted
    if item_price > ordered_at:
        return 'Wait!'
    return round(item_price * item_quantity, 2)
def curry_up_now(item_price):
    """
    >>> curry_up_now(2.99)(2)(15)
    5.98
    <function <lambda>>
    >>> lunch_special = curry_up_now(8.99)
    >>> lunch_special(5)(11)
    44.95
    <function <lambda>>
    >>> lunch_special(3)(13)(2)(14)
    26.97
    8.99
    >>> no_discount = curry_up_now(10.99)(4)(7)
    Wait!
    >>> print(no_discount)
    None
    """
    def order_quantity(item_quantity):
        def by(ordered_at):
            # my answer
            return order_meal(item_price, item_quantity, ordered_at) != 'Wait!' and (print(order_meal(item_price, item_quantity, ordered_at)) or (lambda x: lambda y: order_meal(0.5 * item_price, x, y))) or print(order_meal(item_price, item_quantity, ordered_at))
        return by
    return order_quantity

