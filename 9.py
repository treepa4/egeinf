from functools import lru_cache

@lru_cache(None)
def F(n):
    if n ==41:
        return 41
    if n >41 and n %2==0:
        return F(n-1)-n
    if n > 41 and n%2!=0:
        return n*F(n-2)

for i in range(10000):
    F(i)
print(F(9093)/F(9089))