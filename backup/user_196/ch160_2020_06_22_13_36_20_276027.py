import math
maior = 0
angulo = 0
for x in range (0,91):
    senodebaskara = (4*x*(180-x))/(40500-x*(180-x))
    senoreal = math.sin(math.radians(x))
    diferenca = abs(senodebaskara - senoreal)
    if diferenca > maior:
        maior = diferenca
        angulo = x
print (angulo)
