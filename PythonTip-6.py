a = list(range(2,101))
#c = raw_input('please input:')
b = []
while len(a) > 0:
    c = a[0]
    b.append(c)
    for i in a:
        if i % c == 0:
            a.remove(i)
print(b)