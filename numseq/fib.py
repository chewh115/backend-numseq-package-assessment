"""
Module contains function to return the nth Fibonacci number.
"""


def fib(n):
    """
    returns the nth Fibonacci number. The first 10 terms of the Fibonacci
    sequence are [0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...]
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
