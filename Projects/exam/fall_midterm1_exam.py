"""
Introduced by Tibor Rad¨® in 1962, the Busy Beaver Game aims to find the terminating program of a given length that
produces the most possible output. Here, we¡¯ll explore one approach to generating a lot of output.
Implement b, which takes a zero-argument function f that returns None. The b function calls its argument f 64 times
and returns None.
?You may not use any numbers or strings or any expressions that evaluate to numbers or strings.
?You may not import any functions, but may use built-in functions that do not need to be imported.
?You may not use lists, tuples, or dictionaries.
?Your answer for blank 2 must be no longer than 50 characters, ignoring whitespace
"""

def b(f):
    """Evaluate f() 64 times.
    >>> a = lambda: print('A', end='')
    >>> b(a)
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    """
    (lambda g: g(g(g(g(g(g(f)))))))(lambda h: lambda: h() or h())()


'''
To solve this, we note that 64 = 26, and that there are exactly 6 gs in the lambda. Thus, our strategy to call f 
64 times is as follows:
?Blank 2 should be a function that receives as input a function h and returns a new function that calls h twice.
Since f is guaranteed to return None, we can use h() or h() to call h twice (and return None).
?The first lambda will take in Blank 2 as input g, and run g6on some input. Since each layer of Blank 2 doubles
the number of function calls, g6will call its input function 26= 64 times. This suggests that we should set
Blank 1 to f.
?Therefore, (lambda g: g(g(g(g(g(g(__<BLANK 1>__)))))))(__<BLANK 2>__) creates a function that calls
f() 64 times. We still need to call it, so Blank 3 should call the newly created function. This can be done by
setting Blank 3 to ().
'''
