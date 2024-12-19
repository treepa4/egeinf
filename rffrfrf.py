mASSiv = []
m = 0
for n in range(4, 10000):
    ass = '3' + '5' * n
    while '333' in ass or '555' in ass:
        if ('555' in ass):
            ass = ass.replace('555', '3', 1)
        else:
            ass = ass.replace('333', '5', 1)
    m = max(m, sum([int(x) for x in ass]))
print(m)