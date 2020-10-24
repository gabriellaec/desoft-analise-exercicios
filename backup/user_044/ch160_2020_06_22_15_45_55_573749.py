import math
maior_diferenca = 0
ang = 0
for i in range(91):
    senx = (4*i*(180-i))/(40500-i*(180-i))
    mat = math.sin(math.radians(i))
    diferenca = abs(senx-mat)
    if diferenca > maior_diferenca:
        maior_diferenca = diferenca
        ang = i
print(ang)