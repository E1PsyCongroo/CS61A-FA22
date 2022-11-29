"""This module implements the built-in data types of the Scheme language, along
with a parser for Scheme expressions.

In addition to the types defined in this file, some data types in Scheme are
represented by their corresponding type in Python:
    number:       int or float
    symbol:       string
    boolean:      bool
    unspecified:  None

The __repr__ method of a Scheme value will return a Python expression that
would be evaluated to the value, where possible.

The __str__ method of a Scheme value will return a Scheme expression that
would be read to the value, where possible.
"""

import numbers
import builtins

from ucb import main, trace, interact
from scheme_tokens import tokenize_lines, DELIMITERS

from buffer import Buffer, InputReader, LineReader
from pair import Pair, nil

# BEGIN SOLUTION NO PROMPT
quotes = {"'": 'quote', '`': 'quasiquote', ',@': 'unquote-splicing', ',': 'unquote'}  # Quotation markers (only used in staff sol)
# END SOLUTION NO PROMPT
# Scheme list parser


def scheme_read(src):
    """Read the next expression from SRC, a Buffer of tokens.

    >>> scheme_read(Buffer(tokenize_lines(['nil'])))
    nil
    >>> scheme_read(Buffer(tokenize_lines(['1'])))
    1
    >>> scheme_read(Buffer(tokenize_lines(['true'])))
    True
    >>> scheme_read(Buffer(tokenize_lines(['(+ 1 2)'])))
    Pair('+', Pair(1, Pair(2, nil)))
    """
    if src.current() is None:
        raise EOFError
    val = src.pop_first()  # Get and remove the first token
    if val == 'nil':
        # BEGIN SOLUTION "PROBLEM 2"
        return nil
        # END SOLUTION
    # BEGIN SOLUTION NO PROMPT ALT="elif val == '(':"
    # Handle square brackets
    elif val in set('(['):
    # END SOLUTION
        # BEGIN SOLUTION "PROBLEM 2"
        if src.current() == ".":
            raise SyntaxError(". cannot be the first token in a list")
        # second argument shouldn't be in student solution
        return read_tail(src, val, {"(": ")", "[": "]"}[val])
        # END SOLUTION
    # BEGIN SOLUTION NO PROMPT ALT="elif val == "'":"
    elif val in quotes:
    # END SOLUTION
        # BEGIN SOLUTION "PROBLEM 3"
        return Pair(quotes[val], Pair(scheme_read(src), nil))
        # END SOLUTION
    elif val not in DELIMITERS:
        return val
    else:
        raise SyntaxError('unexpected token: {0}'.format(val))

# BEGIN SOLUTION NO PROMPT ALT="def read_tail(src):"


def read_tail(src, start_token="(", end_token=")"):
# END SOLUTION
    """Return the remainder of a list in SRC, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    """
    try:
        if src.current() is None:
            raise SyntaxError('unexpected end of file')
        # BEGIN SOLUTION NO PROMPT ALT="elif src.current() == ')':"
        # handle both ) and ] in staff interpreter
        elif src.current() in set(')]'):
        # END SOLUTION
            # BEGIN SOLUTION "PROBLEM 2"
            # this check should only exist in the staff interpreter
            if src.current() != end_token:
                raise SyntaxError("Expected {} to match with {} but got {}".format(
                    end_token,
                    start_token,
                    src.current()
                ))
            src.pop_first()
            return nil
            # END SOLUTION
        # BEGIN SOLUTION NO PROMPT
        elif src.current() == '.':  # Handling of malformed lists. You don't need to understand how this block works.
            src.pop_first()
            expr = scheme_read(src)
            if src.current() is None:
                raise SyntaxError('unexpected end of file')
            if src.pop_first() != ')':
                raise SyntaxError('expected one element after .')
            if builtins.DOTS_ARE_CONS:
                return expr
            else:
                return Pair(Pair("variadic", Pair(expr, nil)), nil)
        # END SOLUTION
        else:
            # BEGIN SOLUTION "PROBLEM 2"
            first = scheme_read(src)
            # the end_token argument shouldn't be in student solutions.
            rest = read_tail(src, start_token, end_token)
            return Pair(first, rest)
            # END SOLUTION
    except EOFError:
        raise SyntaxError('unexpected end of file')

# Convenience methods


def buffer_input(prompt='scm> '):
    """Return a Buffer instance containing interactive input."""
    return Buffer(tokenize_lines(InputReader(prompt)))


def buffer_lines(lines, prompt='scm> ', show_prompt=False):
    """Return a Buffer instance iterating through LINES."""
    if show_prompt:
        # BEGIN SOLUTION NO PROMPT
        # TODO(denero) This doesn't work!
        # END SOLUTION
        input_lines = lines
    else:
        input_lines = LineReader(lines, prompt)
    return Buffer(tokenize_lines(input_lines))


def read_line(line):
    """Read a single string LINE as a Scheme expression."""
    buf = Buffer(tokenize_lines([line]))
    result = scheme_read(buf)
    if buf.more_on_line():
        raise SyntaxError("read_line's argument can only be a single element, but received multiple")
    return result

# Interactive loop


def read_print_loop():
    """Run a read-print loop for Scheme expressions."""
    while True:
        try:
            src = buffer_input('read> ')
            while src.more_on_line():
                expression = scheme_read(src)
                if expression == 'exit':
                    print()
                    return
                print('str :', expression)
                print('repr:', repr(expression))
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print()
            return


@main
def main(*args):
    if len(args) and '--repl' in args:
        read_print_loop()
