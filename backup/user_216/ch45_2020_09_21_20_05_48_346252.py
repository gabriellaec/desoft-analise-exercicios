a = int(input('Número qualquer'))

lista = []

while a > 0:
    lista.append(a)
    a = int(input('Número qualquer'))

i = len(lista) - 1

while i >= 0:
    print(lista[i])
    i -= 1
