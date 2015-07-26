"""The infix operator decorator"""

from __future__ import print_function

__all__ = ['shift_infix', 'and_infix', 'or_infix', 'xor_infix', 'pow_infix',
          'mul_infix', 'add_infix', 'sub_infix', 'mod_infix', 'make_infix',
          'all_infix','div_infix', 'floordiv_infix']

from functools import update_wrapper
import sys

def lname(op):
    """The left name of an op"""
    return '__' + op + '__'

def rname(op):
    """The right name of an op, switches shifts"""
    shifts = set(['lshift', 'rshift'])
    if op in shifts:
        op = list(shifts - set([op]))[0]
    return '__r' + op + '__'

class base_infix(object):
    """The base infix class"""
    
    op = () # The operations to use
    
    def __init__(self, function):
        """Creates the decorated function"""
        self._function = function
        update_wrapper(self, self._function)
        ldict = dict()
        rdict = dict()
        for op in self.op:
            ldict[lname(op)] = lbind.__call__
            rdict[rname(op)] = rbind.__call__

        self.lbind = type('_'.join(self.op)+'_lbind', (lbind,), ldict)
        self.rbind = type('_'.join(self.op)+'_rbind', (rbind,), rdict)

    @property
    def __call__(self):
        """Wraps self"""
        return self._function
    
    def left(self, other):
        """Returns a partially applied infix operator"""
        return self.rbind(self._function, other)

    def right(self, other):
        return self.lbind(self._function, other)

# Allows binding
# Idea from http://code.activestate.com/recipes/384122-infix-operators/

class rbind(object):
    def __init__(self, function, binded):
        self._function = function
        update_wrapper(self, self._function)
        self.binded = binded
    def __call__(self, other):
        return self._function(other, self.binded)
    def reverse(self, other):
        return self._function(self.binded, other)
    def __repr__(self):
        return "<{0.__class__.__name__}: Waiting for left side>".format(self)

class lbind(object):
    def __init__(self, function, binded):
        self._function = function
        update_wrapper(self, self._function)
        self.binded = binded
    def __call__(self, other):
        return self._function(self.binded, other)
    def reverse(self, other):
        return self._function(other, self.binded)
    def __repr__(self):
        return "<{0.__class__.__name__}: Waiting for right side>".format(self)
    
def make_infix(*ops):
    """Returns a custom infix type, using the given operation."""
    ops = list(ops)
    if 'div' in ops:
        ops += ['truediv']
    opdict = dict(op=ops)
    for op in ops:
        opdict[lname(op)] = base_infix.left
        opdict[rname(op)] = base_infix.right
    return type('_'.join(ops)+'_infix', (base_infix,), opdict)

def custom_infix(left, right = None):
    """Legacy support for old notation."""
    op = left[3:-2]
    return make_infix(op)

or_infix = make_infix('or')
mul_infix = make_infix('mul')
pow_infix = make_infix('pow')
shift_infix = make_infix('rshift')
and_infix = make_infix('and')
add_infix = make_infix('add')
sub_infix = make_infix('sub')
mod_infix = make_infix('mod')
xor_infix = make_infix('xor')
div_infix = make_infix('div')
floordiv_infix = make_infix('floor_div')
all_infix = make_infix('or', 'and', 'pow', 'mul', 'xor', 'lshift',
                       'rshift', 'sub', 'mod', 'floordiv', 'div')

if __name__ == "__main__":
    from doctest import testfile
    failure_count, test_count = testfile('README.rst', globs=locals())
    if failure_count > 0:
        sys.exit(1)
