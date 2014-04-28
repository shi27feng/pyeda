"""
Boolean Vector Logic Expressions

This module is deprecated.
The functionality has been superceded by the bfarray module.

Interface Functions:
    bitvec
    uint2bv
    int2bv
"""

from warnings import warn

from pyeda.boolalg import expr
from pyeda.boolalg import bfarray

def bitvec(name, *dims):
    """Return a new array of given dimensions, filled with Expressions.

    Parameters
    ----------
    name : str
    dims : (int or (int, int))
        An int N means a slice from [0:N]
        A tuple (M, N) means a slice from [M:N]
    """
    if dims:
        return bfarray.exprvars(name, *dims)
    else:
        return expr.exprvar(name)

def uint2bv(num, length=None):
    """Convert an unsigned integer to an farray of Expressions."""
    warn("vexpr.uint2bv is deprecated. Use bfarray.uint2exprs instead.")
    return bfarray.uint2exprs(num, length)

def int2bv(num, length=None):
    """Convert a signed integer to an farray of Expressions."""
    warn("vexpr.int2bv is deprecated. Use bfarray.int2exprs instead.")
    return bfarray.int2exprs(num, length)

