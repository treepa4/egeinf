# def f(s,m):
#     if s > 66: return m%2==0
#     if m ==0: return 0
#     if s < 67:
#         h= [f(s+1, m-1),f(s*2, m-1)]
#     return any(h) if m%2!=0 else all(h)
#
# print('19', [s for s in range(1,67) if f(s,2)])
# print('20', [s for s in range(1,67) if f(s,3) and (not(f(s,1)))])
# print('21', [s for s in range(1,67) if f(s,4) and (not(f(s,2)))])

# def f(s,m):
#     if s > 99: return m%2==0
#     if m == 0: return 0
#     if s <100: h = [f(s+7,m-1),f(s*2,m-1)]
#     return any(h) if m % 2 != 0 else any(h)
#
# print('19', [s for s in range(1,100) if f(s,1) and f(s,2)])
# print('20', [s for s in range(1,100) if f(s,1) and f(s,2)])


# 8477
# def f(s,m,sn):
#     if s >= (sn + 215)/1.25: return  m%2==0
#     if m == 0: return 0
#     if s < (sn + 215)/1.25:
#         h = [f(int(s*1.25),m-1, sn), f(int(s*1.5),m-1, sn),
#              f(int(s*1.75),m-1, sn), f(int(s*2.1),m-1, sn)]
#         return  any(h) if m%2!=0 else all(h)
#
# print('19', [s for s in range(4,173) if f(s,2, s)])
# print('20', [s for s in range(4,173) if f(s,3, s) and not f(s,1, s) ])
# print('21', [s for s in range(4,173) if f(s,4, s) and not f(s,2, s)])

# def f(s, m):
#     if s >41: return m%2==0
#     if m == 0: return 0
#     if s < 42:
#         # if s % 2 != 0:
#         h = [f(s+1, m-1), f(s+5, m-1), f(s*3, m-1)]
#         # else:
#         #     h = [f(s + 1, m - 1), f(s + 2, m - 1)]
#         return any(h) if m%2!=0 else all(h)
# print([s for s in range(1,41+1) if f(s,2) and not f(s, 1)])
# print([s for s in range(1,41+1) if not f(s,1) and not f(s, 3)])
