# 2
# print("X Y Z W")
# for x in  0,1:
#     for y in  0,1:
#         for z in  0,1:
#             for w in  0,1:
#                 if ((x & (not(y))) or (y == z) or (not(w)))==0:
#                     print(x,y,z,w)
# #
# #5
# for n in range(128, 256):
#     s = bin(n)[2:]  # перевод в двоичную систему
#     s = str(s)
#     s = s.replace('1', '*')
#     s = s.replace('0', '1')
#     s = s.replace('*', '0')
#     r = int(s, 2)  # перевод в десятичную систему
#     if n - r == 185:
#         print(n)
# #
#14
# a = 2*729**333+2*243**334-81**335+2*27**336-2*9**337 -338
# k=0
# while a>0:
#     if a%9>0:
#         k+=1
#     a//=9
# print(k)
# #15
# a = 49**7 + 7**20 - 28
# b=''
# while a>0:
#     b= str(a%7) + b
#     a//=7
# print(b.count('6'), b)
# a = {0: "А", 1: "О", 2: "У"}
# k = 0
# for i in range(0, len(a)):
#     for j in range(0, len(a)):
#         for g in range(0, len(a)):
#             for m in range(0, len(a)):
#                 for n in range(0, len(a)):
#                     k += 1
#                     if a[i] == "О":
#                         print(k) # Возьмем первое число, которое выведет программа
#                         break
# def F(n):
#     if n == 0:
#         return 0
#     if n % 3 == 0 and n > 0:
#         return n + F(n - 3)
#     if n % 3 > 0:
#         return n + F(n - (n % 3))
# print(F(22))