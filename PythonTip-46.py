#-- coding: utf-8 --
#以下代码是受到威佐夫博弈的启发，根据奇异态势的方法写的
a, b =22, 13

if a > b:
    a, b = b, a
s, t = list(range(1, b)), []

for j in range(1, b):
    try:
        t.append([s[0], s[0] + j])
        s.remove(s[0] + j)
        s.remove(s[0])
    except:
        break
#print(t)
if [a, b] in t:
    print('Loose')
else:
    print('Win')