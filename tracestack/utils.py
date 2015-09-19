"""Gets a single character from the user.  Works cross-platform.

Thanks to Danny Yoo (http://code.activestate.com/recipes/134892/)
"""
from __future__ import print_function

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self, msg):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self, msg):
        import msvcrt
        return msvcrt.getch()


class _Getch:
    """Gets a single character from standard input.  Does not echo to the
    screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self, msg): 
        print(msg, end="")
        return self.impl(msg)



getch = _Getch()