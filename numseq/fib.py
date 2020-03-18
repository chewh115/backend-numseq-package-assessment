def fib(n):
    a, b = 0, 1
    for _ in range(1, n):
        total = a + b
        a, b = b, total
    print(total)
    return total
