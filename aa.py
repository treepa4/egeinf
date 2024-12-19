# 14
# for a in range(36,2,-1):
#    try:
#        num = (int('LANCELOT', a)+int('ELSA', a)-int('DRAGON', a)+int('CAT', a))
#        if num %1747==0: print(num/1747)
#    except:
#        continue

# 15
# for a in range(100):
#     for x in range(100):
#         for y in range(100):
#             if (((y + x) ** 2 > 1048) or ((x + 20) < a) and (40 - y < a)) == 1:
#                 print(a)

#16
# from functools import lru_cache
# @lru_cache(maxsize=None, typed=False)
# def F(n):
#     if n<=10: return 2*n
#     if n % 2 == 0 and n>10: return F(n-3) - F(n - 9) * 2
#     if n % 2 != 0 and n >10: return F(n-2) * 2 - F(n-7)
#
#
# for i in range(3000):
#     F(i)
#
# print(sum([int(s) for s in str(F(3063))]))

#19-21
# def f(s,m):
#     if s > 65534: return m%2==0
#     if m == 0: return 0
#     if s <65535: h = [f(s+1,m-1),f(s+2,m-1),f(s+4,m-1),f(s+8,m-1),f(s+16,m-1),f(s+32,m-1),f(s*3,m-1),f(s*9,m-1),f(s*27,m-1)]
#     return any(h) if m % 2 != 0 else all(h)
#
# print('19', [s for s in range(65000) if not(f(s,1)) and f(s,2)])
# print('20', [s for s in range(65000) if (f(s,3)) and not(f(s,1)) ])