"""Provides combinator functions"""
from ._curry import curry


def I(x):
    """Ix = x"""
    return x


@curry
def K(x, y):
    """Kxy = x"""
    return x


@curry
def B(x, y, z):
    """Bxyz = x(yz)"""
    return x(y(z))


@curry
def C(x, y, z):
    """Cxyz = xzy"""
    return x(z)(y)


@curry
def D(x, y, z, w):
    """Dxyzw = xy(zw)"""
    return x(y)(z(w))


@curry
def E(x, y, z, w, v):
    """Exyzwv = xy(zwv)"""
    return x(y)(x(w)(v))


@curry
def F(x, y, z):
    """Fxyz = zyx"""
    return z(y)(x)


@curry
def G(x, y, z, w):
    """Gxyzw = xw(yz)"""
    return x(w)(y(z))
