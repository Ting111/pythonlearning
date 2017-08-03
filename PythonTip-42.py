from math import sqrt
n = 188
def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def total(n):
    s = 0
    for i in range(2, n // 2):
        if is_prime(i) and is_prime(n - i):
            s += 1
            print(i, '+', n - i)
    return s

print(total(n))