# https://education.yandex.ru/ege/variants/e55c8be4-c3e4-4ed0-9d72-0f359575205b/
#1

#2
from itertools import  product, permutations
def f (a,b,c,d):
    return ( ( a <= b ) and ( b <= c ) and (c <= d) )

for p in permutations('abcd'):
    for a1,a2 in product([0,1], repeat = 2):
        table = [(0,a1,1,0,1),
                 (0,a2,1,0,1),
                 (0,1,1,1,1)]
        if len(set(table)) == len(table):
            if all(f(**dict(zip(p, row))) == row[-1] for row in table):
                print(*p)
                break
print((2560*1440)/8/1024/1024/1024*200)





from itertools import permutations
table = '4 46 47 123567 47 24 345'.split()
graph = 'AB GB GF FB FE EB DB DC CB'.split()
print('1 2 3 4 5 6 7')
for p in permutations('ABCDEFG'):
    if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
        print(*p)
        break
