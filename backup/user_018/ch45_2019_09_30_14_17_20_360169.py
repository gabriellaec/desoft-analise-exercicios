lista = [1,2,-3,-4]

def zera_negativos (x):
    i=0
    for i in lista:
        if i <= 0:
            lista[i] = 0
        i += 1
    return lista

     