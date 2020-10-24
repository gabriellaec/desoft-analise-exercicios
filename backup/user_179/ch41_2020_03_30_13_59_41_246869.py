lista = [-1,1,-2,2,-3,3,-4,4]
def zera_negativos(lista):
    i = 0
    lenght = len (lista)
    while i < lenght:
        if lista[i] < 0:
            lista[i] = 0
            i = i + 1
        else: 
            i = i + 1
            