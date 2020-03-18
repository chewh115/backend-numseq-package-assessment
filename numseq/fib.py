def fib(n):
    """Returns nth Fibonacci number"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
