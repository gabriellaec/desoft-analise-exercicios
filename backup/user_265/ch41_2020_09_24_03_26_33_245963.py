lista = [1, -2, 3, -4, 5]
nova = []

i = 0

def zera_negativos(lista):
    while i < len(lista):
        if lista[i] < 0:
            nova += 0
            i += 1
        else: 
            nova += lista[i]
            i += 1

    return nova