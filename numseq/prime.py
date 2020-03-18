# I found this stack overflow to be VERY helpful
# specifically to keep 9 from being a prime number:
# https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python


def primes(n):
    """Returns a list of all prime numbers less than n"""
    prime_list = []
    if n > 1:
        for i in range(2, n+1):
            prime = True
            for j in range(2, i):
                if i % j == 0:
                    prime = False
                    print(f'{i} is not a prime')
                    break
            if prime:
                prime_list.append(i)
    print(prime_list)
    return prime_list


def is_prime(m):
    if m > 1:
        for num in range(2, m):
            if m % num == 0:
                print(f'{m} is not a prime number. It is divisible by {num}')
                return False
        print(f'{m} is a prime number')
        return True
