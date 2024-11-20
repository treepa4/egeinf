from fnmatch import fnmatch

f = open('24.txt').read().split('&')
m = []
for i in range(1, len(f)):
    if f[i - 1].count('.') > 0 and f[i].count('.') > 0:
        b1 = f[i - 1].split('.')[-2] + '.' + f[i - 1].split('.')[-1]
        b2 = f[i].split('.')[0] + '.' + f[i].split('.')[1]
        a = b1 + '&' + b2
        if fnmatch(a, '*.*&????.*') and (a.count('.') == 2) \
                and (f[i - 1].split('.')[0] != '') and \
                (len(str(int(f[i - 1].split('.')[0]))) == 4) and ('&0' not in a):
            print(a)
            m.append(len(a))
print((max(m)))
