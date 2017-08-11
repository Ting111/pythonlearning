s='202.a.3.24'

def f(s):

    if s.count('.') != 3:
        return 'No'
    else:
        a = s.split('.')
        for i in a:
            if i not in map(str,range(256)):
                return 'No'
        return 'Yes'

print(f(s))