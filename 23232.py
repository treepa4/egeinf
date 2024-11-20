from functools import lru_cache
@lru_cache(None)
def f(x,y):
    if  y == 15:
        ans.add(x)
        return
    f(x + 1, y+1),
    f(x * 2, y+1),
    f(x * 3, y+1)
ans = set()
for i in range(2,15,2):
    f(i,0)
print(len(ans))
