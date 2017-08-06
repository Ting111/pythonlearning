L = [1, 1]
while n > len(L):
    L.append((L[-1] + L[-2]) % 20132013)
print(L[-1])