# -- coding: utf-8 --
#此答案能通过部分

def f(L):
    a = sum(L) / 4
    m, n = [], a
    while True:
        s = len(L)
        if m != []:
            n = m[-1]
            m = []
        if n == min(L):
            return False
            break
        L.sort()
        x = L[-1]
        #print('start:', L)
        L2 = L[:s-1]
        for i in L2[::-1]:
            if x+i <= a and i < n:
                m.append(i)
                x += i
        if x == a:
            L.remove(L[-1])
            if m != []:
                for j in m:
                    L.remove(j)
            m, n = [], a
        #print('end:  ',L)
        #print('----------')
        if L == []:
            return True
            break

if len(L) < 4 or sum(L)%4 != 0 or max(L) > sum(L)/4:
    print('No')
else:
    if f(L):
        print('Yes')
    else:
        print('No')