lista = [5,-3,5,2,9]
def zera_negativos(lista):
    i=0
    while i < 5:
        if lista[i] < 0:
            lista[i] = 0       
       	i += 1
    return (lista)
