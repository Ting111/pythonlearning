x = [n]
while True:
    for i in x:
        for j in w:
            if i >= j:
                x.append(i % j)
    if x[0] != 0:
        del x[0]
    if 0 in x:
        print('Yes')
        break    
    if max(x) < min(w):
        print('No')
        break