# -- coding: utf-8 --
def s(a, n):# 10进制数变为n进制数(string)

    d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    a, b = int(a), ''
    while a > 0:
        if a % n < 10:
            b += str(a % n)
        else:
            b += d[a % n]
        a = a // n   
    return b[::-1]

def f(a, n):# n进制数变为10进制数(int)

    d = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    a, b = str(a), 0
    a = a[::-1]
    for i in range(len(a)):
        if a[i] not in 'ABCDEF':
            b += int(a[i]) * n**i
        else:
            b += d[a[i]] * n**i
    return b

def h(m, n):

    step = 0
    while m != m[::-1]:
        m = f(m, n) + f(m[::-1], n)
        m = s(m, n)
        step += 1
        if step > 30:
            return 0
            break
    return step

print(h(M, N))