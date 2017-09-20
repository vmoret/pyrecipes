"""Partial applicative functions"""
from functools import wraps


def partiall(func, *args, **kwargs):
    """partiall(func, *a, **b) -> (*c, **d) --> func(*a, *c, **b, **d)"""
    @wraps(func)
    def wrapper(*argv, **kws):
        return func(*args, *argv, **kwargs, **kws)
    return wrapper


def partialr(func, *args, **kwargs):
    """partialr(func, *a, **b) -> (*c, **d) --> func(*c, *a, **d, **b)"""
    @wraps(func)
    def wrapper(*argv, **kws):
        return func(*argv, *args, **kws, **kwargs)
    return wrapper

