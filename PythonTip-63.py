# -- coding: utf-8 --
#能通过部分情况
L = [5, 13, 7]

L.sort()
while True:
    a, m, h, s = L[:], 0, 0, 0
    while len(a) > 0:
        i = a[-1]
        del a[-1]
        if h < m:
            h += i
        elif m < h:
            m += i
        else:
            s = m
            m += i
    if m == h:
        s = m
    if s == 0 and len(L) > 0:
        del L[-1]
    else:
        print(s)
        break