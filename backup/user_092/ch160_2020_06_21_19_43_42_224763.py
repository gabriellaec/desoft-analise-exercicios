import math
i = 0
L = []
while i<=90:
    a = i*(180-i)
    b = 4*a
    c = 40500 - a
    bha = b/c
    
    e = math.radians(i)
    f = math.sin(e)
    g = math.degrees(f)
    L.append(abs(d+g))
    i+=1
print(max(L))