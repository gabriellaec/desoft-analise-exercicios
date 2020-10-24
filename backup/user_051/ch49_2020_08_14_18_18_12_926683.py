def inverte_lista(x):
    lista_i=[]
    for i in range(len(x)-1):
        lista_i.append(x[len(x)-1-i])
    return lista_i