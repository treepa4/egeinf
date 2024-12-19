# f = [int(i) for i in open('17_12926.txt').read().split()]
f = [int(i) for i in open('17 (1).txt', 'r')]
# m = [int(i) for i in range(0,len(f)-3) if (str(f[i])[-1] == str(f[i+1])[-1] and str(f[i+1])[-1] == str(f[i+2])[-1] and str(f[i+2])[-1] == str(f[i+3])[-1])]
print(f)