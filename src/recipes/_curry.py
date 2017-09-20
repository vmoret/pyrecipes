"""Provides curry decorator"""
from functools import wraps
from inspect import getfullargspec


class Function(object):
    """Callable class used to represent a curried function"""

    __slots__ = ('__func',)

    def __init__(self, func):
        self.__func = func

    def __call__(self, *args):
        func = self.__func
        for arg in args:
            if callable(func):
                func = func(arg)
            else:
                raise TypeError('Too many arguments for curried function')
        return func


def curry(func):
    """
    Function decorator tranforming `func` to a curried function

    >>> @curry
    ... def add(x, y):
    ...     return x + y
    ...

    >>> add(1, 2)
    3

    >>> add(1)(2)
    3
    """
    argcount = len(getfullargspec(func).args)
    def build(args, k):
        @wraps(func)
        def wrapper(x):
            return build(args + [x], k - 1)
        return func(*args) if k == 0 else wrapper
    return Function(build([], argcount))

