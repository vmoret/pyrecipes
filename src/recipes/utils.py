"""Utilities functions"""
import csv
from collections import namedtuple

from .itertools import foldr

__all__ = ('read_csv', 'compose')


def snake_case(s):
    """snake_case(s) --> s

    >>> snake_case('Service Order ID')
    'service_order_id'

    """
    return ''.join(c if c.isalnum() else '_' for c in s.lower())


def read_csv(file, encoding=None, delimiter=','):
    """read_csv(file[, encoding, delimiter]) --> generator"""
    with open(file, 'r', encoding=encoding) as fp:
        reader = csv.reader(fp, delimiter=delimiter)
        R = namedtuple('R', tuple(map(snake_case, next(reader))))
        yield from (R(*x[:-1]) for x in reader)


def compose(*funcs):
    """compose(a, b, ...z) --> z(...b(a))"""
    *rest, func = *funcs
    def inner(self, *args, **kwargs):
        value = func(*args, **kwargs)
        return value if len(rest) == 0 else compose(*rest)(value)
    return inner

