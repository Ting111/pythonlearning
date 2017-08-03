p = 2992

def sum_sys(num, sys):
    total = 0
    while num > 0:
        total += num % sys
        num = num // sys
    return total

x, y, z = sum_sys(p, 10), sum_sys(p, 12), sum_sys(p, 16)
if x == y and y == z:
    print('YES')
else:
    print('NO')