from itertools import permutations
table = '67 346 24 235 47 127 156'.split()
graph = 'ГД ГВ ВД АК АБ КБ КЕ ДЕ ВБ'.split()
# print(table)
print('1 2 3 4 5 6 7')
for p in permutations('АБВГДЕК'):
    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
        print(*p)
        break