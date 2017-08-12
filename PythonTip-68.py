from itertools import *

L = [4,41,414,4141,4145]

# answer_1:
m = []
for i in permutations(L, len(L)):
    m.append(int(''.join(map(str, i))))
print(max(m))

# answer_2:
L.sort(lambda a,b:int(str(b)+str(a))-int(str(a)+str(b)))
print(''.join(map(str,L)))