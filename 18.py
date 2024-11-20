f = open('18.txt', 'r')
mas = []
for i in f:
    mas.append([int(j) for j in  i.split()])
# print(mas)
mas_2 = [[0]*len(mas[0]) for _ in range(len(mas))]
mas_2[-1][0] = mas[-1][0]
# print(mas_2)
for i in range(1, len(mas)):
    mas_2[-1][i] = mas_2[-1][i-1] + mas[-1][i]
for i in range(len(mas), -2, -1):
    mas_2[i][0] = mas_2[i+1][0] + mas[i][0]
for i in range(1, len(mas)):
    for j in range(1, len(mas)):
        mas_2[i][j]=max(mas_2[i][j-1], mas_2[i-1][j], mas_2[i-1][j-1])+mas[i][j]
print(*mas_2, sep='\n')