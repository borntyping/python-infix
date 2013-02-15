"""The infix operator decorator"""

__all__ = ['infix']

from functools import update_wrapper

class Infix(object):
    """The base infix class, which infix types are based on"""
    
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

def __update_attributes(attributes, left, right):
    attributes.update({
        left: Infix.left,
        right: Infix.right,
    })

def infix(function=None, operator='shift', all=False, custom=None):
    """Creates an infix decorator type"""
    
    attributes = dict()

    if custom is not None:
        __update_attributes(attributes, custom[0], custom[1])
    else:
        if operator in ('<<', '>>', 'shift') or all:
            __update_attributes(attributes, '__rlshift__', '__rshift__')

        if operator in ('|', 'or') or all:
            __update_attributes(attributes, '__ror__', '__or__')

        if operator in ('^', 'xor') or all:
            __update_attributes(attributes, '__rxor__', '__xor__')

    # Create the infix type with the attributes selected
    infix_type = type('infix', (Infix,), attributes)

    # Allow the decorator to be called without arguments
    return infix_type(function) if function is not None else infix_type

if __name__ == "__main__":
    from doctest import testfile
    testfile('README.rst', globs={
        'infix': infix,
    })
