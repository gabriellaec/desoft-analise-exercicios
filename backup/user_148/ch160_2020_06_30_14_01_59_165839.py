import math

lista_sin = []
lista_for = []
lista_dif = []

for i in range(0, 90):
    ang = math.radians(i)
    lista_sin.append(math.sin(ang))
    x = 4*i*(180 - i)/(40500 - i*(180 - i))
    lista_for.append(x)

    lista_dif.append(lista_for[i] - lista_sin[i])

print(lista_dif.index(max(lista_dif)))
