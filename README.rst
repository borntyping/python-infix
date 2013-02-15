=====
Infix
=====

A decorator that allows functions to be used as infix functions

Infix operators are created and applied as such::

    >>> @infix
    ... def plus(a, b):
    ...     return a + b
    ...
    >>> print 40 <<plus>> 2
    42
    >>> print plus(5, 5)
    10

The operator can still be used normally.

Variant syntaxes
----------------

Different types of infix operators can be created by passing a ``operator`` argument to ``@infix``::

    >>> @infix(operator='|')
    ... def minus(a, b):
    ...     return a - b
    ...
    >>> print 1 |minus| 2
    -1

    >>> @infix(operator='^')
    ... def until(start, stop):
    ...     return range(start, stop)
    ...
    >>> print 1 ^until^ 10
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

The infix syntaxes and the aliases that ``@infix`` takes for them:

- ``<<infix>>``: ``'<<'``, ``'>>'``, ``'shift'``
- ``|infix|``: ``'|'``, ``'or'``
- ``^infix^``: ``'^'``, ``'xor'``

Custom syntaxes
----------------

Python has a large set of operators than could be overridden to provide the infix syntax, so instead of providing them all ``@infix`` can take custom parameters::

    >>> @infix(custom=('__rmod__', '__mod__'))
    ... def ate(a, b):
    ...     return (a == 7 and b == 9)
    ...
    >>> print 7 %ate% 9
    True
    >>> print 6 %ate% 7
    False

The ``custom`` parameter is a tuple consisting of the name of a `right operand <http://docs.python.org/2/reference/datamodel.html#object.__radd__>`_ and a `left operand <http://docs.python.org/2/reference/datamodel.html#object.__add__>`_. You should be careful to avoid using operands that the objects your functions will take may provide themselves (as the initial right operand is only called if the previous object does not provide for that operator).

