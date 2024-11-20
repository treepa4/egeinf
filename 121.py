def f(s1, s2, m):
    if s1+s2 >= 189: return m%2==0
    if m==0: return 0

    h = [ f(s1+s2,s2,m-1), f(s1,s2+s1,m-1)]
    if s1 < s2:
        h.append( f(s1+(s2-s1),s2,m-1) )
    elif s2 < s1:
        h.append( f(s1,s2+(s1-s2),m-1) )

    return any(h) if m%2!=0 else all(h)

print( [i for i in range(1,184) if (f(5,i,2) or f(5,i,4)) and (not(f(5,i,2))) ] )