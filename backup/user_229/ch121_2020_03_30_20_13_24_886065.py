lista3 = []

def subtração_de_listas(lista1, lista2):
    i = 0
    f = 0
    while lista1[i] not in lista2:
        lista3[f] = lista1[i]
        i += 1
        f += 1
    return lista3

print(subtração_de_listas)
        