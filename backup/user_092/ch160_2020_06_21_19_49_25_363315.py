import math
i = 0
L = []
while i<=90:
    a = i*(180-i)
    b = 4*a
    c = 40500 - a
    bha = abs(b/c)
    
    e = math.radians(i)
    f = math.sin(e)
    g = math.degrees(f)
    pad = abs(g)
    L.append(abs(bha-pad))
    i+=1

c = 0
while c <= len(L): 
    if L[c] == max(L):
        print(c)