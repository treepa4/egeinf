# def f(s1,s2,m):
#     if s1+s2 > 180: return m%2==0
#     if m == 0: return 0
#     h = [f(s1+4,s2, m-1),f(s1*3,s2, m-1),f(s1,s2+4, m-1),f(s1,s2*3, m-1)]
#     return any(h) if m%2!=0 else all(h)


#
# print('19', [s for s in range(1,156) if f(25,s,2)])
# print('20', [s for s in range(1,156) if f(25, s,3) and not f(25,s, 1)])
# print('21', [s for s in range(1,156) if f(25, s,4) and not f(25,s, 2)])
#
# def d (n):
#     dd = []
#     for x in range(2, int(n**0.5)+1):
#         if n%x==0:
#             dd.append(x)
#             dd.append(n//x)
#     return dd
#
# def f (s,m):
#     if s>45: return m%2==0
#     if m == 0: return 0
#     dd = d(s)
#     h=[]
#     for i in dd:
#         h.append(f(s+s//i, m-1))
#     return any(h) if m%2!=0 else all(h)
#
#
# print('19', [s for s in range(1,46) if f(s, 2)])
# print('20', [s for s in range(1,46) if f(s, 3) and not f(s,1)])
#
# print('21', [s for s in range(1,46) if f(s, 3) and not f(s,1)])

# for i in range(100):
#     n=i
#     binn = bin(n)[2:]
#     s = sum([int(i) for i in str(binn)])
#     binn = str(binn) + str(s%2)
#     s = sum([int(i) for i in str(binn)])
#     binn = str(binn) + str(s % 2)
#     r = int(binn, 2)
#     print(r)

# from itertools import product
# alp = "AОУ"
# m = []
# for i in (product(alp, repeat=5)):
#     m.append(i)
#
# sorted(m)
# print(m[209])

#
# def f(s,r,a,t):
#     return ( (s or ( not(r) ) ) and ( not(r == a) ) and t )
#
# from itertools import permutations, product
# a=set()
#
# for p in permutations('srat'):
#     for a1,a2,a3,a4 in product([0,1], repeat = 4): #кол-во а1,а2... зависит от кол-ва пропусков в таблице истинности
#         table = [[0,1,a1,0,1], #таблица истинности  из условия задания
#                  [a2,1,1,0,1],
#                  [1,a3,0,a4,1]]
#         if table[0] == table[1] or table[1] == table[2]: continue #защита от повторояющихся строк
#         if all([f(**dict(zip(p,row,))) == row[-1] for row in table]):
#             print(*p)
#             m = []
#             m.append(str(*p[0])+str(*p[1])+str(*p[2])+str(*p[3]))
#             print(m)
#
# for i in range (1000,100000):
#     a=[]
#     s=str(i)
#     for j in range (0,len(s)-2):
#         a.append(int(s[j]+s[j+1]+s[j+2]))
#     if (max(a)-min(a)) == 415:
#         print(i)
#         break



# from itertools import permutations
# table = '16'.split()
# graph = 'AC AB CF CD DF FH HG GD GE DE DB BE'.split()
# print('1 2 3 4 5 6 7 8')
# for p in permutations('ABCDEFGH'):
#     if all(str(p.index(c2)+1) in table[p.index(c1)] for c1, c2 in graph):
#         print(*p)
#         break
# from func_perevoda import convert_to
#
# for i in range(100):
#     n = i
#     th_n = convert_to(n, 3)
#     if n %5!=0:
#         n1 = str(n)[0:-2] + str(n)[0]
#


# print( (((1024*2560*13/128)/100)*70)/8/1024 )

# from itertools import product
# alp = 'АКЛПШЮ'
# m =[]
# for i in product(alp, repeat = 5):
#     i=''.join(i)
#     m.append(i)
#     if i.count("Ю")<=1:
#         if i.find("Ю") == 0 and i[i.find('Ю')+1] != "Ш":
#             print(i, m.index(i))
#         elif i.find("Ю") == 4 and i[i.find('Ю')-1] != "Ш":
#             print(i, m.index(i))
#         elif i.find("Ю") != 0 and i.find("Ю") != 4 and i[i.find('Ю')+1] != "Ш" and i[i.find('Ю')-1] != "Ш":
#             print(i, m.index(i))

# for i in range(3500):
#     a = '0'+ '1'*i + '2'*i +'0'
#     while '00' not in a:
#         a = a.replace('011', '20', 1)
#         a = a.replace('022', '10', 1)
#         a = a.replace('01', '220', 1)
#         a = a.replace('02', '110', 1)
#     if a.count('2')>50:
#         if a.count('1') ==40:
#         # print(a.count('2'))
#             print(a, a.count('2'))
# from func_perevoda import convert_to
# a =convert_to( (81**15 + 3**22 - 27) ,9 )
# print(a)

# from functools import lru_cache
# @lru_cache(None)
# def f(n):
#     if n <11: return 10
#     if n >=11: return n + f(n-1)
#
# for i in range(2000):
#     f(i)
#
# print(f(2204)-f(2202))

# print(len(oct(35_184_372_088_832)[2:]), int('1_000_000_000_000_000',8))

# def f(n):
#     print('*')
#     if n >= 1:
#         print('*')
#         f(n - 1)
#         f(n // 2)
# f(2)

# def f(n):
#     print('*')
#     if n >= 1:
#         print('*')
#         f(n - 1)
#         f(n // 2)
#
# print(f(40))

# from itertools import product
# a, k = product("ВЬЮГА", repeat=6), 0
# for i in a:
#     b = ''.join(i)
#     if "ЮГ" in b: k+=1
#
# print(k)

# for i in range(7000,8000):
#     a = '0' + '5'*i
#     while ('55' in a) or ('150' in a) or ('555' in a):
#         if ('55' in a): a=a.replace('55','615',1)
#         if ('150' in a): a = a.replace('150', '5950', 1)
#         if ('555' in a): a = a.replace('555', '50', 1)
#
#     nech = []
#     for i in a:
#         if int(i)%2!=0:
#             nech.append(int(i))
#     bolshiesummki = sum(nech)
#     if bolshiesummki > 100_000: print(i)