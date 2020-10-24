lista = [0,-4,6,8,3,-3,-6,3,6,-8]

def zera_negativos(lista):
    i=0
    while i < len(lista):
        if lista[i] < 0:
            lista[i]=0
        i+=1
    return lista

print(zera_negativos(lista))