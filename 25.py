def f1(n,y):
    if n == y: return 0
    if y != 3:
        if n%5 == 0:
            print(2,n//5)
            return f(n//5,y)
        else:
            print(1,n+3)
            return f(n+3,y)
f(n:30,y:3)