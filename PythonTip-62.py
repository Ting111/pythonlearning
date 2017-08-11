a, b = 98, 89

def f(a, b):
    L = []
    for i in str(b)[::-1]:
        L.append(a * int(i))
    return L

def h(a, b):
    c, d, e = ' ', '-', '-' * 8
    print(c*(8 - len(str(a))) + str(a))
    print('x' + c*(7 - len(str(b))) + str(b))
    print(e)   
    L = f(a, b)
    res,s = 0, L
    for i in range(len(L)):
        res += L[i] * (10**i)       
        s[i] = c*(8 - len(str(L[i])) - i) + str(L[i])
    res =str(res)

    for k in s:
        print(k)
    if len(s) == 1:
        return '*' * 20
    print(e)
    print(c*(8 - len(res)) +res)
    return '*' * 20

print(h(a, b))