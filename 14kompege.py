# result = set()
# for x in range(0,18):
#     for y in range(9,18):
#         if x<y:
#             a = (5 *18**3 + x*18**2 + y *18 +10) + (1*y**3 + 8*y**2 + x*y**1 +7)
#         result.add(a)
# print(len(result))

#7679
# res = set()
# for x in range(1,20):
#     for y in range(1, 20):
#         for t in range(1, 20):
#             num1 = (1*20**2 + x*20**1 + y) + (3*11 + y)
#             num2 = (4*11+y) -(t*8 + 1)
#             if num2 == 0: zn = 0
#             else: zn = num1/num2
#             if zn%5==0:
#                 res.add(zn)
# print(max(res))

#4195
# a = 7*(512**1912) + 6 * (64**1954)- 5 * (8**1980) -2022
# b = ''
# while a>0:
#     b=str(a%8)+b
#     a//=8
# print(b)
# print(b.count('7')-1)
#
#926
# set = set()
# for x in range(0,1000000000):
#     a = 7**500+7**200-7**50
#     b=''
#     while a>0:
#         b=str(a%7)+b
#         a//=7
#
#     if a > 0:
#         bs = sum([int(i) for i in b])
#         set.add(bs)
# print(max(set))
# def prst(n):
#     for i in range(2, a//2+1):
#         if (n%i==0): return 0
#     return 1
# for x in '0123456789ABCDEFGH':
#     a = int('56' + str(x) + '3',18) + int('4' + str(x) + '9', 18) - int('57' + str(x)+'1',18)
#     k=0
#     if prst(a):
#         print(a)
#         k += 1
# print(k)
# a = 5**20+5**10-5**13-5**3
# b = ''
# while a>0:
#     b=str(a%5)+b
#     a//=5
# print(b, sum([int(i) for i in b]))
# ss = '0123456789A'
# for x in ss:
#     a = int('95' + str(x) + '2', 11) + int(str(x) + '458', 12)
#     if a % 136 == 0:
#         print(a/136)

# ss = '01234567'
# for x in ss:
#     for y in ss:
#         a = int(str(x) + '01' + str(y) + '4', 9) + int(str(x)+str(y) + '544',8)
#         if a %89==0:
#             print(a/89)
# a = 3*125**6+2*25**9+5**12-625
# print(a)
# b = ''
# while a>0:
#     b=str(a%5)+b
#     a//=5
# print(b.count('0'))
