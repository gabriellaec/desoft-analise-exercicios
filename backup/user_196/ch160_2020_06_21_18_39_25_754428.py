import math
maior = 0
angulo = 0
def calcula_seno(x):
    senodebaskara = (4*x(180-x))/(40500-x*(180-x))
    for angulo in range (0,91):
        diferenca = senodebaskara - math.degrees(math.sin(angulo))
        if angulo == 0:
            maior = diferenca
        else:
            if diferenca > maior:
                diferenca = maior
    return abs(maior)
    return angulo