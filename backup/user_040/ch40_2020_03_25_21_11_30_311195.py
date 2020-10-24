y=1
def soma_valores(lista):
    while y<len(lista):
        s = lista[y]+lista[y-1]
        y+=1
    return s