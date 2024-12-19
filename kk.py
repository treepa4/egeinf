from functools import lru_cache

@lru_cache(None)
def F(n):
    if n >= 2025: return 1
    if n<2025: return n - F(n+2) - F(n+4)

for i in range(2100,0,-1):
    F(i)

print(F(20) + F(25))