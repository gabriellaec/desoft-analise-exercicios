def zera_negativos(lista_inteiros):
    contador=0
    while contador< len(lista_inteiros):
        if lista_inteiros[contador]<0:
            lista_inteiros[contador]=0
        contador+=1
    return lista_inteiros
    