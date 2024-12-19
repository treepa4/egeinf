# f, k, m = open('24 (2).txt', 'r').readline().split((str.isalpha())), 0, []
# f = filter
# f = ''.join(f)
# print(f)

f = open('24.txt', 'r').read()
ALP_LEN = 17
counter = 0
for i in range(0, len(f)-(ALP_LEN+1),ALP_LEN):

    # print(set(f[i:i+26]))
    if len((set(f[i:i+ALP_LEN]))) == ALP_LEN:
        counter+=1
print(counter)