import math
angulo = 0
valor = 0
while angulo <= 90:
    angulo.radians()
    bask = (4*angulo*(180-angulo))/(40500-angulo*(180-angulo))
    norm = math.sin(angulo)
    if abs(bask-norm) > valor:
        valor = abs(bask-norm)
    elif abs(norm-bask) > valor:
        valor = abs(norm-bask)
    angulo.degrees()
    angulo += 1
print(valor)