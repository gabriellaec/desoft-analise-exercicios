import math
maior = 0
angulo = 0
for x in range (0,91):
    senodebaskara = (4*x*(180-x))/(40500-x*(180-x))
    diferenca = abs(senodebaskara - math.sin(math.radians(x)))
    if diferenca > maior:
        diferenca = maior
        angulo = x
print (angulo)
