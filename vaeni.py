def nod(m,n):
    if m%n==0: return n
    if n%m==0: return m
    n1 = [i for i in range (2,(n//2)+1) if n%i ==0]
    m1 = [i for i in range (2,(m//2)+1) if m%i ==0]
    for i in range(len(n1)-1,0,-1):
        if n1[i] in m1: return n1[i]
print(nod( 111111111, 333773373737))


