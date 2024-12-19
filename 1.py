from itertools import permutations
table = '3457 456 167 128 126 2358 138 467'.split()
graph = 'LK LR LA LP KB KR RC BC CA CQ AQ BP QP'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('LKRAQCBP'):
    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
        print(*p)
        break
