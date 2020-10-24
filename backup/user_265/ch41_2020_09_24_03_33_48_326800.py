lista = [1, -2, 3, -4, 5]

def zera_negativos(lista):
    i = 0
    a = 0
    nova = []
    while a < len(lista):
        if lista[i] < 0:
            nova += '0'
            a += 1
        else: 
            nova += lista[i]
            a += 1

    return nova