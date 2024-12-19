#2
# from itertools import permutations, product
# a= set()
# def f(x,y,z,w):
#     return ( ( w <= (not(x)) ) == ( z <= y ) ) and (y or w)
#
#
# for p in permutations('xyzw'):
#     for a1,a2 in product([0,1], repeat = 2):
#         table = [[1,1,1,1,0],
#                  [0,0,1,1,1],
#                  [0,a1,0,a2,1]]
#         if table[0] == table[1] or table[1] == table[2]: continue
#         if all([f(**dict(zip(p,row,))) == row[-1] for row in table]):
#             print(*p)

#5
# m=[]
# for i in range(456_789_012, 456_000_000 + 1, -1):
#     n=i
#     bn = bin(n)[2:]
#     if n%2==0: bn = '11' + str(bn)
#     if n%2!=0: bn = '1' + str(bn) + '10'
#     r = int(bn, 2)
#     m.append(r)
# print(max(m))

#7
# print(320*640*8 / 8 / 1024)

#16
# def f(n):
#     if n>= 2000: return 2000
#     if n < 2000 and n%2 != 0: return n *f(n+1)
#     if n < 2000 and n%2 == 0: return n * ((f(n+1))/2)
#
# print(f(1998)/f(2001))

#12
# a = '0' + 10*'1' + 10*'2' + '0'
# while '00' not in a:
#     a=a.replace('012', '30', 1)
#     if '011' in a:
#         a=a.replace('011', '20',1)
#         a=a.replace('022', '40',1)
#     else:
#         a=a.replace('01', '10',1)
#         a=a.replace('02', '101',1)
#
# print(a)

#9
# count = 0
# for s in open('9.txt'):
#     M = [int(x) for x in s.split()]
#     minm, maxm = min(M), max(M)
#     A = [x for x in M if x != minm and x!= maxm]
#     # B = [x for x in M if M.count(x) == 1]
#     if len(M) == len(set(M)) and ((maxm+minm)/2) > sum(A)/4:
#         count+=1
#
# print(count)

#17
k=0
f = open('17.txt', 'r')
print(*f)
M = [int(x) for x in f if int(x)%2==0]
ll = [int(x) for x in f]
try:
    sr = sum(M)/len(M)
except any:
    continue
for i in range(0, len(ll)):
    if (ll[i] % 3 ==0 and ll[i+1] <sr and ll[i+1] % 3 != 0) or (ll[i+1] % 3 ==0 and ll[i] <sr and ll[i] % 3 != 0):
        k+=1

print(k)