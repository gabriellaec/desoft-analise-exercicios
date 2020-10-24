def numero_no_indice(lista):
    lista=[]
    for i in len(lista):
        if lista[i]==i:
            lista.append(lista[i])
    return lista