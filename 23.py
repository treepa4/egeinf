# def f(x, y):
#     if x > y or x == 33:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 1, y) + f(x * 2, y)
# print(f(3, 16) * f(16, 37))
#
from functools import lru_cache
@lru_cache(None)
def f(x,y):
    if x ==y: return 1
    if x<y or x==42: return 0
    return f(x-1,y) + f(x//3,y) + f(x//4, y)

for x in range(252,2025): f(x, 250)
print(f(2025,250)*f(250,25))