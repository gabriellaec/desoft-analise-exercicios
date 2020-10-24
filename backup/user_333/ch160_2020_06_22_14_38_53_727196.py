import math

diferenca_max = 0
for angulo in range(0,91,1):
    senbhas = (4*angulo*(180-angulo))/(40500-(angulo*(180-angulo)))
    senpyth = math.sin(angulo)
    diferenca = senpyth-senbhas
    diferenca = abs(diferenca)
    if diferenca > diferenca_max:
        diferenca_max = diferenca
        
print(diferenca_max)
    