def f(x):
    
    x1 = x.copy()
    x1.sort()
    x2 = x1.copy()
    x2.reverse()
    if x == x1:
        return 'UP'
    elif x == x2:
        return 'DOWN'
    else:
        return 'WRONG'
    
L = [1, 2, 4, 5, 7] 
print(f(L))