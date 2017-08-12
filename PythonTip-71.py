from math import *

def isprime(n):

    if n == 1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def t(n):

    L = []
    while isprime(n) == False:
        for i in range(2, n):
            if isprime(i):
                if n % i == 0:
                    L.append(i)
                    n = n // i
                    break
    L.append(n)
    return L

def h(n):

    L = [i for i in range(2, n+1)]
    L1 = []
    for i in L:
        if isprime(i):
            continue
        else:
            L1.append(i)
            
    for i in L1:
        L.remove(i)
    L2 = [t(i) for i in L1]

    L1 = []
    for i in L2:
        for j in i:
            L1.append(j)

    L1 += L
    L2 = []
    for i in L:
        x = L1.count(i)
        if x != 1:
            s = str(i) + '^' + str(x)
        else:
            s = str(i)
        L2.append(s)
    return str(n) + '=' + '*'.join(L2)

print(h(6))