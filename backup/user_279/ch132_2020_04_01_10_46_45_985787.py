import math
def calcula_trabalho(F,coso,s):
    t = F * math.cos(math.radians(coso)) * s
    return t

coso = 0
F = 10
s = 5
trab = calcula_trabalho(F,coso,s)
print(trab)

