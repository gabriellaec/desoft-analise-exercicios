import math

def bhaskara (angulo):
    sen = (4*angulo*(180-angulo))/(40500-(angulo*(180-angulo)))
    return sen

def senpy (angulo):
    sen = math.sin(angulo)
    return sen

diferenca_max = 0
for angulo in range(0,91):
    senbhas = bhaskara(angulo)
    senpyth = senpy(angulo)
    diferenca = senbhas - senpyth
    diferenca = abs(diferenca)
    if diferenca > diferenca_max:
        diferenca_max = diferenca
        
print(diferenca_max)
    