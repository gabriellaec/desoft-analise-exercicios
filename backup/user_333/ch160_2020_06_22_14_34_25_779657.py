import math

def bhaskara (angulo):
    sen = (4*angulo*(180-x))/(40500-(x*(180-x)))
    sen = abs(sen)
    return sen

def senpy (angulo):
    angulo = math.radians(angulo)
    sen = math.sin(angulo)
    sen = abs(sen)
    return sen

diferenca_max = 0
diferenca = 0
for angulo in range(91):
    senbhas = bhaskara(angulo)
    senpyth = senpy(angulo)
    diferenca = senbhas - senpyth
    diferenca = abs(diferenca)
    if diferenca > diferenca_max:
        diferenca_max = diferenca
        
print(diferenca_max)
    