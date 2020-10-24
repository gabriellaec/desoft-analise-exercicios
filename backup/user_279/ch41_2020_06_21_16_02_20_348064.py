lista = [2,3,-1,6,-3]
def zera_negativos():
    i=0
    while i < len(lista):
        if lista[i] < 0:
            lista[i] = 0
            i= i+1
        else:
            i=i+1
    return lista
    