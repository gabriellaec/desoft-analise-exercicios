lista = [1, -2, 3, -4, 5]

def zera_negativos(lista):
    i = 0
    a = 0
    nova = []
    while i < len(lista):
        if lista[a] < 0:
            nova += '0'
            i += 1
        else: 
            nova += lista[a]
            i += 1

    return nova