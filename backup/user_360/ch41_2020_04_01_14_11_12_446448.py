def zera_negativos(lista):
    cont=0
    while cont< len(lista):
        if lista[cont]<0:
            lista[cont]==0
        else:
            pass
            cont+=1
    return lista