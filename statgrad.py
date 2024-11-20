# zywx
# print('X Y Z W')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 if (((x<=y)==(y<=z))&(y or w)) == True: print(x,y,z,w)

# m = []
# for n in range(100, 5500):
#     m = [int(str(n)[j:j+3]) for j in range(len(str(n))-2) ]
#     if max(m)- min(m) == 415: print(n); break

# from itertools import product
# k,l = 0, 'КНРС'
# a = list(product('АЕКНРС', repeat = 10))
# for i in range(2,len(a),3):
#     if a[i][0] in l:
#         if a[i].count('Р') == 1: k+=1
# print(k)


# def is_prime(x):
#     for i in range(2, (x//2)+1):
#         if x % i == 0:
#             return False
#     return True
#
# m=[]
# for i in range(1000):
#     for n in range(0,10000):
#         a = '0'+ '3'*n + '4'*i +'0'
#         m = [int(i) for i in a]
#         while (not('00' in a)):
#             a = a.replace('033', '21120', 1)
#             a = a.replace('034', '22120', 1)
#             a = a.replace('04', '220', 1)
#             a = a.replace('030', '100', 1)
#         if len(a) == 65 and is_prime(sum(m)) == True: print(n)

# for n in range(1, 100):
#     s = bin(n)[2:]
#     if n % 2 == 0:
#         s += "00"
#     else:
#         s += "11"
#     r = int(s, 2)
#     if r > 115:
#         print(n)
#         break
#
# for i in range(100,1000):
#     fst = str(i)
#     num = int((fst[0])) + int((fst[1]))
#     num1 = int(fst[1]) + int(fst[2])
#     a = str(max(num1, num)) + str(min(num1, num))
#     if a == '159': print(i); break

from functools import lru_cache
# cache = lru_cache(f(n))
# или

# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return F(n - 2) * (n + 1)
# print(F(8))
# def third(n):
#     trd = ''
#     while n > 0:
#         trd = str(n % 3) + trd
#         n //= 3
#     return trd
#
# b=''
# r = 0
# for n in range(100):
#     sy = third(n)
#     if n%3==0: sy = sy + sy[-2:]
#     else: sy = sy + third((n//3)*5)
#     if len(sy) == 5 and int(sy)>11221: print(sy)
#     # r = int(sy, 3)
# print(int('12020', 3))
# # print(third(133))
#
# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n >= 2024: return 1
#     return f(n+2) + (n+4)

# print(f(2024))
# k=0
# a =[]
# b = []
# f = open("17.txt", "r").read().split()
# for i in f:
#     if int(i)%1001: b.append(i)
#
# max1001 = max(b)
# for j in range(1, len(f)):
#     if ((len(f[j]) == 3) or (len(f[j-1]) == 3)) and (sum(int(f[j]), int(f[j-1]))>max1001):
#         a.append((sum(int(f[j]), int(f[j-1]))))
#         k+=1
#
# print(k, min(a))
# my_string = "На вилах ехал Иван"
#
# s = my_string.lower()
#
# nospaced = ''.join(s.split())
#
# reversed = nospaced[::-1]
#
# print(nospaced==reversed)
#
# m=[]
# for n in range(4,10_000):
#     s = '8' + n*'5'
#     while ('8858' in s) or ('555' in s):
#         if '8858' in s:
#             s = s.replace('8858', '4', 1)
#         else: s = s.replace('555', '58')
#         if '5858' in s: s = s.replace('5858', '85', 1)
#
#     for i in s:
#         i = int(i)
#         m.append(i)
#     if sum(m) == 66:
#         print(n)

print(27/72)