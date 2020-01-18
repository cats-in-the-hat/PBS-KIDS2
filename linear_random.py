from zgulde.ds_imports import *
from inspect import getsource
from itertools import *
from typing import *


def is_list_sorted(l):
    for curr, nxt in and_next(l):
        if nxt is not None and curr > nxt:
            return False
    return True

# import itertools as it

def drop(xs, n):
    return it.islice(xs, n, None)

def and_next(xs):
    """
    Return each of the items in the iterable xs, along with the next item.
    When the iterable is exhausted, the last item is None.
    Returns
    -------
    An iterable of tuples, where each tuple is the current item and the next
    item.
    >>> list(and_next([1, 2, 3]))
    [(1, 2), (2, 3), (3, None)]
    """
    return it.zip_longest(xs, drop(xs, 1))