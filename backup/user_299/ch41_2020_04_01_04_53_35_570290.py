def zera_negativos (lista_zuada):
    i=0
    while i<len(lista_zuada):
        if lista_zuada[i]<0:
            lista_zuada[i]=0
            i=i+1
        else:
            i=i+1
    return lista_zuada
