def zera_negativos (lista):
    substituidos=[]
    i=0
    while i < len(lista):
        if lista[i] < 0 or lista[i] == 0:
            substituidos.append(lista[i])
            i+=1
        else:
            i+=1
    return (substituidos)