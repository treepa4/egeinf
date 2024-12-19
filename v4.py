from itertools import permutations
table = '24 146 56 1267 36 23457 46'.split()
graph = 'АБ БВ ФВ ВД ВЕ ВГ ДЕ ЕГ ЕК КГ'.split()
print('1 2 3 4 5 6 7')
for p in permutations('АБВГДЕК'):
    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
        print(*p)
        break
