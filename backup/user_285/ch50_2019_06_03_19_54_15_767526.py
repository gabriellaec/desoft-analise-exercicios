def numero_no_indice(lista):
    lista1=[]
    for i in len(lista):
        if lista[i]!=i:
            lista1.append(lista[i])
    return lista1