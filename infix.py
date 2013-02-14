"""The infix decorator"""

__all__ = ['infix']

from functools import update_wrapper

class partial(object):
    """A partially applied infix object

    This is the result of ``obj << infix``"""
    
    def __init__(self, infix, left):
        self.infix = infix
        self.left = left

    def __rshift__(self, right):
        return self.infix(self.left, right)

class infix(object):
    """A decorator that makes a function into an infix operator

    The infix operator can then be applied as such::

        left <<infix_function>> right

    For example:

    >>> @infix
    ... def plus(a, b):
    ...     return a + b
    
    >>> print 1 <<plus>> 2
    3

    The operator can still be used normally
    >>> print plus(1, 2)
    3
    """
    def __init__(self, func):
        """Decorates ``func``"""
        update_wrapper(self, func)
        self.func = func
    
    def __call__(self, left, right, *args, **kwargs):
        """Applies the function"""
        return self.func(left, right, *args, **kwargs)

    def __rlshift__(self, left):
        """Returns a partially applied infix operator"""
        return partial(self, left)

if __name__ == "__main__":
    from doctest import testmod
    testmod()
