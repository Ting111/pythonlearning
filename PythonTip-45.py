# -- coding:utf-8 --
w, n = [2, 1], [1, 2]
#下面的解法是网友写的
W = {0}
L = {0}
for i,v in enumerate(n):
    for j in range(v+1):
        L.add(j * w[i])
    W = {x+y for x in W for y in L}
    L = {0}
print(len(W))