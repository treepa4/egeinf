count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    minm, maxm = min(M), max(M)
    A = [x for x in M if x != minm and x!= maxm]
    B = [x for x in M if M.count(x) == 1]
 
        count+=1

print(count)