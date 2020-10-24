import math

def arcotangente(x, n):
    l = []
    l.append(x)
    j = 3
    i=0
    while i<n:
        l.append((x**j)/j)
        i+=1
        j+=2
    w = 0
    r = 1
    while i<len[l]:
        l[r].append(l[r]*(-1))
        w+=1
        r+=2 
    return sum(l)
