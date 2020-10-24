import math
d_maior = 0
for x in range (91):
    sin = (4 * x * (180 - x)) / (40500 - x * (180 - x))
    a = math.sin(math.radians(x))
    diferenca = abs (a - sin)
    if diferenca > d_maior:
        d_maior = diferenca
        angulo = x   
print(angulo)
