"""Provides itertools"""
from ._curry import curry
from functools import reduce

__all__ = ('map', 'filter', 'foldl', 'foldl2')


@curry
def map(func, iterable):
    """map(func, iterable) --> generator"""
    return (func(x) for x in iterable)


@curry
def filter(func, iterable):
    """filter(func, iterable) --> generator"""
    return (x for x in iterable if func(x))


@curry
def foldl(func, sequence, initial):
    """foldl(func, sequence, initial) --> value"""
    return reduce(func, sequence, initial)


@curry
def foldl2(func, sequence):
    """foldl2(func, sequence) --> value"""
    return reduce(func, sequence, None)

