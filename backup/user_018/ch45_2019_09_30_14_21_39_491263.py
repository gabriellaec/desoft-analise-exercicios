lista = [1,2,-3,-4]

def zera_negativos (x):
    i=0
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] =0
    return lista

     