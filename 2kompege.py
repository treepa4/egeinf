# from itertools import product
# print("X Y Z W F")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if (((w<=y)<=x) or (not(z))) == 0: print(x, y,z, w, '0')
# zywx


# print("X Y Z W")
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if ( (x and (not(y)) ) or (x==z) and (not(w)) ) == 0: print(x, y,z, w)
# zyxw

#
# print('C A T S ')
# for c, a, t, s in product((0, 1), repeat = 4):
#     if (((not(c)) <= (not(a))) or (not(t <=s)) or c) == 0:
#         print(c, a, t,s)


# x y z w
#
# 1 0 1 0
# 1 0 1 1


# from itertools import permutations, product
# a=set()
# def f(x,y,z,w): #описание функции
#     return (((x==z) <= ( (not(y)) or w ) == (not(((w <=z ) or (x<=y))))))
#
# for p in permutations('xyzw'):
#     for a1,a2,a3,a4,a5 in product([0,1], repeat = 5): #кол-во а1,а2... зависит от кол-ва пропусков в таблице истинности
#         table = [[a1,1,a2,0,1], #таблица истинности  из условия задания
#                  [0,a3,1,a4,1],
#                  [0,a5,0,0,1]]
#         if table[0] == table[1] or table[1] == table[2]: continue #защита от повторояющихся строк
#         if all([f(**dict(zip(p,row,))) == row[-1] for row in table]):
#
#             m = []
#             m.append(str(*p[0])+str(*p[1])+str(*p[2])+str(*p[3]))
#             print(m)
from itertools import permutations, product
a=set()
def f(x,y,z,w):
    return ( not( ( ( ( ( ( ( w and x ) == x ) or 1 ) <= z ) or (not(x)) ) and y ) ) )

for p in permutations('xyzw'):
    for a1,a2,a3,a4 in product([0,1], repeat=4):
        table = [ [a1,a2,1,0,0],
                  [1,a3,1,0,0],
                  [a4,0,0,1,0]]
        if table[0]== table[1] or table[1] == table[2]: continue
        if all([f(**dict(zip(p,row,))) == row[-1] for row in table]):
            print(*p)