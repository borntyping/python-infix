"""The infix operator decorator"""

from __future__ import print_function

__all__ = ['shift_infix', 'and_infix', 'or_infix', 'xor_infix']

from functools import update_wrapper

class base_infix(object):
    """The base infix class"""
    
    def __init__(self, func):
        """Creates the decorated function"""
        self.func = func
        update_wrapper(self, self.func)

    @property
    def __call__(self):
        """Wraps self"""
        return self.func
    
    def left(self, left):
        """Returns a partially applied infix operator"""
        self.__infix__ = left
        return self

    def right(self, right):
        return self.func(self.__infix__, right)

class shift_infix(base_infix):
    __rlshift__ = base_infix.left
    __rshift__ = base_infix.right

class and_infix(base_infix):
    __rand__ = base_infix.left
    __and__ = base_infix.right

class or_infix(base_infix):
    __ror__ = base_infix.left
    __or__ = base_infix.right

class xor_infix(base_infix):
    __rxor__ = base_infix.left
    __xor__ = base_infix.right

def custom_infix(left, right):
    """Returns a custom infix type, using the given left and right function
    names"""
    return type('custom_infix', (base_infix,), {
        left: base_infix.left,
        right: base_infix.right,
    })

if __name__ == "__main__":
    from doctest import testfile
    failure_count, test_count = testfile('README.rst', globs=locals())
    if failure_count > 0:
        exit(1)
