def fib(n):
    """Returns nth Fibonacci number"""
    a, b = 0, 1
    for _ in range(1, n):
        total = a + b
        a, b = b, total
    print(total)
    return total
