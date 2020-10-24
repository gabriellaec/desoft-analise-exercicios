lista = [1, -2, 3, -4, 5]
nova = []



def zera_negativos(lista):
    i = 0
    while i < len(lista):
        if lista[i] < 0:
            nova += 0
            i += 1
        else: 
            nova += lista[i]
            i += 1

    return nova