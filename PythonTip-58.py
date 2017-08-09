L.sort()

while len(L) > 1:
    for i in range(1, L[0]+1):
        b = i * L[1]
        if b % L[0] == 0:
            del L[0]
            L[0] = b
            break

print(L[0])