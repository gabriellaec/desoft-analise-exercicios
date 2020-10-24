import math
dif = 0 
for g in range(0,91):
    funcao = math.sin(math.radians(g))
    bhask = (4*g*(180-g))/(40500 - g*(180-g))
    if abs(funcao - bhask) > dif:
        dif = abs(funcao - bhask)
        grau = g

print(grau)
