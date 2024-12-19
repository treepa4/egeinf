A = set()


# for a in range(1,100):
#     f = True
#     for x in range(1,100):
#         for y in range(1,100):
#             if (((x+y)<25) or (y<(x-1)) or (y >=a))==0:
#                 f = False
#                 break
#     if f: A.add(a)
#     print(A)

# for a in range(1,1100):
#     f = True
#     for x in range(1,200):
#         for y in range(1,200):
#             if ((2*y > 5*x) or (x*y < a) or ( x > 21)) ==0:
#                 f = False
#                 break
#     if f: A.add(a)
# print(min(list(A)))
# print(A)
for a in range(1,1000):
    f = True
    for x in range(1,1000):
        for y in range(1,1000):
            if ( (x%100!=0) and (x%4==0) ) or (x%400==0) or (x%a!=0) ==0:
                f = False
                break
    if f: A.add(a)
print(A)

#HOД
# def nod(n,m,k):
#     d1 = []
#     d2 = []
#     for i in range(2, int(n**0.5)+1):
#         if n %i ==0:
#             d1.append(n//i)
#             break
#     for i in range(2, int(m**0.5)+1):
#         if m %i ==0:
#             d2.append(m//i)
#             break
#     if len(d1)>0 and len(d2)>0:
#         return d1[0]==d2[0]==k

# def nod(a,b,k):
#     while a != b:
#         if a > b:
#             a = a - b
#         if b > a:
#             b = b - a
#     return a==k
# c=0
# for a in range(1,1001):
#     f=True
#     for x in range(1,1001):
#         if ((nod(a,420,2) or ((nod(a,x,12) or not(nod(110,x,11))))))==0:
#             f=False
#     if f==True:
#         c+=1
# print(c)


