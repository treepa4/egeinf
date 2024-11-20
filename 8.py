from itertools import product
alp = "АРТЕМ"

k=0
for i in product(alp, repeat = 5):
    # i = ''.join(i)
    if ( ( (i[0] not in 'АЕ' ) and (i[-1] not in 'АЕ' ) ) or ((i[0] not in 'АЕ' ) and (i[-1] in 'АЕ' )) or ((i[-1] not in 'АЕ' ) and (i[0] in 'АЕ' )) ) and len(i) == len(set(i)):
        k+=1

print(k)