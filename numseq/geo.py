"""
Module contains functions to find nth number in geometric squared,
geometric triangle and geometric cubed functions.
"""


def sqaure(n):
    """
    Returns the nth term of the numbers that can be arranged into square
    geometric shapes [1, 4, 9, 16, 25 ... ]
    """
    return n*n


def triangle(n):
    """
    Returns the nth term of the numbers that can be arranged in triangular
    geometric shapes [1, 3, 6, 10, 15, 21, 28, 36, 45, 55 ... ]
    """
    return sum(range(1, n+1))


def cube(n):
    """
    Returns the nth term of the numbers that can be arranged as
    symmetric cube shapes [1, 8, 27, 64 ...]
    """
    return n**3
