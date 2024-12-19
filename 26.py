f = [int(i) for i in open('28139.txt', 'r')]
f.pop(0)
m = []
k=0
for i in range(0, len(f)-1):
    if (f[i] % 2 ==0 and f[i+1] % 2 ==0) or (f[i] % 2 !=0 and f[i+1] % 2 !=0) and ((f[i] + f[i+1]) in f):
        k+=1
        m.append(f[i]+f[1+i])

print(k, m, max(m))


