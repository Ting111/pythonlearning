#-- coding: utf-8 --
L = 'caayyhheehhbzbhhjhhyyaac'

size = len(L)
length = -1
maxup = -1
maxdown = -1

for i in range(size-1):

    if L[i] == L[i+1]:#中心字母有两个
        down = i
        up = i + 1

    if (L[i] != L[i+1]
            or (i - 1 >= 0
                and L[i] == L[i-1]
                and L[i] == L[i+1])):#中心字母为一个
        down = i
        up = i

    while True:
        if (down - 1 >= 0
                and up + 1 < size
                and L[down-1] == L[up+1]):
            down -= 1
            up += 1
        else:
            if length < up - down + 1:
                length = up - down + 1
                maxdown = down
                maxup = up
            break

print(L[maxdown : maxup+1])