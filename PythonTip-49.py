a, b = -132874894578, 16

def f(a, b):
    n = ''
    d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    flag = True

    if a == 0:
        return 0

    if a < 0:
        a = -a
        flag = False

    while a > 0:
        x = a % b
        a = a // b
        if x < 10:
            n = str(x) + n
        else:
            n = d[x] + n

    if flag:
        return n
    else:
        return '-' + n

print(f(a, b))