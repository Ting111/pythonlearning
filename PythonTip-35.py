L=[-2,-3,3,50,1,60,7,-4,8,6,36,2,4,-5,-7,141,12]
b=[0]*len(L)

for e in range(0,len(L)):
    if e==0:
        b[e]=L[0];
    else:
        b[e]=max(b[e-1]+L[e],L[e])


print(max(b))