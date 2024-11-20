n=int(input())
a=int(input())
x=int(input())
b=int(input())
y=int(input())
c={}
if x in c:
    c[x]+=a
else:
    c[x]=a
if y in c:
    c[y]+=b
else:
    c[y]=b
pos=1
ans=[]
while pos<=n:
    max_cr=-1
    opt=None
    for r in c:
        if c[r]>0:
            pr=min(n,pos+r)
            cr=pr+r
            if pr-r<=pos and cr>max_cr:
                max_cr=cr
                opt=(pr,r)
    if opt:
        ans.append(f"{opt[0]} {opt[1]}")
        c[opt[1]]-=1
        pos=opt[0]+opt[1]+1
    else:
        print(-1)
        exit()
print('\n'.join(ans))
