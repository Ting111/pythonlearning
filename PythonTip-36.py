L=[-2,-3,3,50,1,60,7,-4,8,6,36,2,4,-5,-7,141,12]
b=[0]*len(L)

for e in range(len(L)):
    if e == 0 or e == 1:
        b[e] = L[e];
    else:
        b[e] = max(max(b[: e-1]) + L[e], L[e])


print(max(b))