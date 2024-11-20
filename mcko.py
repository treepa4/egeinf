# for d in range(0,40): print(d*11 % ((5-1)*(7-1)) == 1, d)
# print("X Y W F")
# for x in 0,1:
#     for y in 0,1:
#         for w in 0,1:
#             if (x & (w <= y)) == 1:
#                 print(x,y,w, '1')
#             if (x & (w <= y)) == 0:
#                 print(x,y,w, '0')
#
#
from itertools import product, permutations
def f(a,b,c,d):
    return (c and (a or d) and (d <= b)) == 1
for per in permutations('abcd'):
    for a1,a2,a3,a4,a5,a6 in product([0,1], repeat = 16):
        table = [(a1,a2, a3, 0, 1),
                 (a4,1,0, a5, 1),
                 (0,a6,1,0,1)]
        if len(set(table)) == len(table):
            if all(f(**dict(zip(per, row))) == row[-1] for row in table):
                print(*per)
                break
# альтернативное решение

from functools import lru_cache
# def f(n):
#     if n > 2023: return 1
#     else: return f(n+2)+f(n+4)

















