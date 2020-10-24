import math
d = []
for x in range (91):
    sin = (4 * x * (180 - x)) / (40500 - x * (180 - x))
    a = math.sin(math.radians(x))
    diferenca = abs (a - sin)
    d.append(diferenca)
    i = 0
    while i < len(d):
        d_maior = 0
        if d[i] > d_maior:
            d_maior = d[i]
            angulo = x
        i += 1

print (angulo)