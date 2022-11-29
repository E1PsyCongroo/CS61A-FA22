"""The buffer module assists in iterating through lines and tokens."""

import math
import sys

# BEGIN SOLUTION NO PROMPT
if sys.version_info[0] < 3:  # Python 2 compatibility
    def input(prompt):
        sys.stderr.write(prompt)
        sys.stderr.flush()
        line = sys.stdin.readline()
        if not line: raise EOFError()
        return line.rstrip('\r\n')
# END SOLUTION


class Buffer:
    """A Buffer provides a way of accessing a sequence of tokens across lines.

    Its constructor takes an iterator, called "the source", that returns the
    next line of tokens as a list each time it is queried, or None to indicate
    the end of data.

    The Buffer in effect concatenates the sequences returned from its source
    and then supplies the items from them one at a time through its pop_first()
    method, calling the source for more sequences of items only when needed.

    In addition, Buffer provides a current method to look at the
    next item to be supplied, without sequencing past it.

    The __str__ method prints all tokens read so far, up to the end of the
    current line, and marks the current token with >>.
    >>> buf = Buffer(iter([['(', '+'], [15], [12, ')']]))
    >>> buf.pop_first()
    '('
    >>> buf.pop_first()
    '+'
    >>> buf.current()
    15
    >>> buf.current()   # Calling current twice should not change buf
    15
    >>> buf.pop_first()
    15
    >>> buf.current()
    12
    >>> buf.pop_first()
    12
    >>> buf.pop_first()
    ')'
    >>> buf.pop_first()  # returns None
    """

    def __init__(self, source):
        """
        Initialize a Buffer instance based on the given source.
        """
        self.index = 0
        # BEGIN SOLUTION NO PROMPT
        self.lines = []
        # END SOLUTION
        self.source = source
        self.current_line = ()
        self.current()

    def pop_first(self):
        """Remove the next item from self and return it. If self has
        exhausted its source, returns None."""
        # BEGIN SOLUTION "PROBLEM 1"
        current = self.current()
        self.index += 1
        return current
        # END SOLUTION

    def current(self):
        """Return the current element, or None if none exists."""
        # BEGIN SOLUTION "PROBLEM 1" NO PROMPT ALT="while _________:"
        while not self.more_on_line():
        # END SOLUTION
            try:
                # BEGIN SOLUTION "PROBLEM 1"
                self.index = 0
                self.current_line = next(self.source)
                # END SOLUTION
                # BEGIN SOLUTION NO PROMPT
                self.lines.append(self.current_line)
                # END SOLUTION
            except StopIteration:
                self.current_line = ()
                return None
        # BEGIN SOLUTION "PROBLEM 1" NO PROMPT ALT="return __________"
        return self.current_line[self.index]
        # END SOLUTION

    def more_on_line(self):
        return self.index < len(self.current_line)

    # BEGIN SOLUTION NO PROMPT
    def __str__(self):
        """Return recently read contents; current element marked with >>."""
        # Format string for right-justified line numbers
        n = len(self.lines)
        msg = '{0:>' + str(math.floor(math.log10(n)) + 1) + "}: "

        # Up to three previous lines and current line are included in output
        s = ''
        for i in range(max(0, n - 4), n - 1):
            s += msg.format(i + 1) + ' '.join(map(str, self.lines[i])) + '\n'
        s += msg.format(n)
        s += ' '.join(map(str, self.current_line[:self.index]))
        s += ' >> '
        s += ' '.join(map(str, self.current_line[self.index:]))
        return s.strip()
    # END SOLUTION


# Try to import readline for interactive history
try:
    import readline
except:
    pass


class InputReader:
    """An InputReader is an iterable that prompts the user for input."""

    def __init__(self, prompt):
        self.prompt = prompt

    def __iter__(self):
        while True:
            yield input(self.prompt)
            self.prompt = ' ' * len(self.prompt)


class LineReader:
    """A LineReader is an iterable that prints lines after a prompt."""

    def __init__(self, lines, prompt, comment=";"):
        self.lines = lines
        self.prompt = prompt
        self.comment = comment

    def __iter__(self):
        while self.lines:
            line = self.lines.pop(0).strip('\n')
            if (self.prompt is not None and line != "" and
                not line.lstrip().startswith(self.comment)):
                print(self.prompt + line)
                self.prompt = ' ' * len(self.prompt)
            yield line
        raise EOFError
