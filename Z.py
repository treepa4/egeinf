# from itertools import permutations, product
# a=set()
# def f(x,y,z,w): #описание функции
#     return ( (not( y <= ( x == w ) )) and ( z <= x ) )
#
# for p in permutations('xyzw'):
#     for a1,a2,a3,a4,a5 in product([0,1], repeat = 5): #кол-во а1,а2... зависит от кол-ва пропусков в таблице истинности
#         table = [[a1,1,1,a2,1], #таблица истинности  из условия задания
#                  [0,a3,a4,0,1],
#                  [a5,0,1,0,1]]
#         if table[0] == table[1] or table[1] == table[2]: continue #защита от повторояющихся строк
#         if all([f(**dict(zip(p,row,))) == row[-1] for row in table]):
#
#             m = []
#             m.append(str(*p[0])+str(*p[1])+str(*p[2])+str(*p[3]))
#             print(m)

# for i in range(2000):
#     n=i
#     b = bin(n)[2:]
#     # print(b)
#     b = b[:-1]
#     # print(b)
#     if n % 2 ==0: b = b + '01'
#     else: b = b +'10'
#     r = int(b, 2)
#     # print(r)
#     if r == 2018: print(i)

# print(1600*1200*4/8/1024/1024)
from itertools import product
k=0
for i in product( 'оиа','плн', 'оиа', 'плн'):
    k+=1

print(k)