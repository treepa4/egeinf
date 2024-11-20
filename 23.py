from functools import lru_cache
@lru_cache(None)
# def f(x, y):
#     if y == 4:
#         ans.add(x)
#         return
#     f(x+2, y+1)
#     f(x*3, y+1)
#
# ans = set()
# f(1, 0)
# print(ans)
def f(x,y):
    if x>y : return 0
    if x==y: return 1
    return f(x+2,y)+f(x*3,y)
print(f(1,25))